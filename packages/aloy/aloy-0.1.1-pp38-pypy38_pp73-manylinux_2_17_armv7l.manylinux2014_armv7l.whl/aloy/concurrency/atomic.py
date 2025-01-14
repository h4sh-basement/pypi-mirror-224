###########################################################################
###########################################################################
## Module containing classes defining mutable atomic objects.            ##
##                                                                       ##
## Copyright (C) 2023 Oliver Michael Kamperis                            ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## any later version.                                                    ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the          ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program. If not, see <https://www.gnu.org/licenses/>. ##
###########################################################################
###########################################################################

"""
Module containing classes defining mutable atomic objects.

Atomic objects are thread-safe objects whose updates are atomic.
They are useful for concurrent programming, where multiple threads
may be accessing or updating the same object, but where the updates
may happen over a large function block and not in a single call,
therefore it is important to ensure that the object is not changed
by another thread during the update.

Updates are only allowed within a context manager, accessing an
object (through a function that does not change the object) may
be called outside of a context manager, but will be blocking if
the object is currently being updated by another thread.
"""

from abc import ABCMeta, abstractmethod
import collections.abc
import sys
import types
from typing import (
    Any, Callable, Concatenate, Generic, Hashable, Iterable, Iterator,
    Mapping, ParamSpec, TypeVar, final, overload
)
from aloy.concurrency.synchronization import OwnedRLock

__copyright__ = "Copyright (C) 2023 Oliver Michael Kamperis"
__license__ = "GPL-3.0"

__all__ = (
    "AloyAtomicObjectError",
    "AtomicObject",
    "AtomicNumber",
    "AtomicBool",
    "AtomicList",
    "AtomicDict",
    "AtomicSet"
)


def __dir__() -> tuple[str, ...]:
    """Get the names of module attributes."""
    return __all__


class AloyAtomicObjectError(RuntimeError):
    """An exception raised when an error occurs in an atomic object."""


SP = ParamSpec("SP")
ST = TypeVar("ST")


def _atomic_require_lock(
    func: Callable[Concatenate[Any, SP], ST]
) -> Callable[Concatenate[Any, SP], ST]:
    """
    Decorator that ensures the object is locked by current thread, and
    therefore is not being updated by another thread before calling the
    method.
    """
    def wrapper(self: Any, *args: SP.args, **kwargs: SP.kwargs) -> ST:
        with self:
            return func(self, *args, **kwargs)
    return wrapper


def _atomic_require_context(
    func: Callable[Concatenate[Any, SP], ST]
) -> Callable[Concatenate[Any, SP], ST]:
    """
    Decorator that ensures the object is locked and being updated within
    a context manager before calling the method.
    """
    def wrapper(self: Any, *args: SP.args, **kwargs: SP.kwargs) -> ST:
        self._check_context()  # pylint: disable=protected-access
        return func(self, *args, **kwargs)
    return wrapper


AT = TypeVar("AT")


class _Atomic(Generic[AT], metaclass=ABCMeta):
    """Base class for atomic objects."""

    __slots__ = {
        "__lock": "The lock used to ensure atomic updates."
    }

    def __init__(self) -> None:
        """Create a new atomic object."""
        self.__lock = OwnedRLock()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.get_obj()!s}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.get_obj()!r})"

    @_atomic_require_lock
    @abstractmethod
    def get_obj(self) -> AT:
        """Returns the wrapped object."""
        ...

    @_atomic_require_context
    @abstractmethod
    def set_obj(self, value: AT, /) -> None:
        """Sets the wrapped object."""
        ...

    def __enter__(self) -> "_Atomic":
        self.__lock.acquire()
        return self

    def __exit__(
        self,
        exc_type: type | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None
    ) -> None:
        self.__lock.release()

    def _check_context(self) -> None:  # pylint: disable=unused-private-member
        """Check that the object is currently being updated."""
        if not self.__lock.is_locked:
            raise AloyAtomicObjectError(
                "Cannot update atomic object outside of a context manager."
            )
        if not self.__lock.is_owner:
            raise AloyAtomicObjectError(
                "Attempted to update atomic object from a non-owner thread."
            )


OT = TypeVar("OT")


@final
class AtomicObject(_Atomic[OT]):
    """
    A thread-safe atomic object wrapper.

    Getting the wrapped object is only allowed whilst another thread does not
    have the object locked. The object is locked whilst a thread has entered
    the object's context manager, and is unlocked when the thread exits the
    context manager. Setting the wrapped object is only allowed within a
    context manager. This allows one to ensure that the object is not got
    by another thread whilst it is being updated by multiple operations
    in another thread, therefore making those operations atomic.

    Note that this does not make accesses/updates to the wrapped object itself
    thread-safe, it only ensures that access to the object through the wrapper
    is thread-safe. Therefore, if the wrapped object is a mutable object, and
    another thread keeps a reference to the object, then it is possible for
    that thread to change the object even whilst it does not have the atomic
    lock.
    """

    __slots__ = {
        "__object": "The object being wrapped."
    }

    def __init__(self, object_: OT, /) -> None:
        """Create a new atomic object."""
        super().__init__()
        self.__object: OT = object_

    @_atomic_require_lock
    def get_obj(self) -> OT:
        """Returns the wrapped object."""
        return self.__object

    @_atomic_require_context
    def set_obj(self, object_: OT, /) -> None:
        """Sets the wrapped object."""
        self.__object = object_


NT = TypeVar("NT", int, float, complex)


@final
class AtomicNumber(_Atomic[NT]):
    """
    A thread-safe number whose updates are atomic.

    Updates to the number are only allowed within a context manager.
    """

    __slots__ = {
        "__value": "The current value of the number."
    }

    def __init__(self, value: NT = 0) -> None:
        """
        Create a new atomic number with given initial value.

        The number type can be int, float, or complex.
        """
        super().__init__()
        self.__value: NT = value

    @_atomic_require_lock
    def get_obj(self) -> NT:
        """Returns the current value of the number."""
        return self.__value

    @_atomic_require_context
    def set_obj(self, value: NT, /) -> None:
        """Sets the number to the given value."""
        self.__value = value

    @_atomic_require_lock
    def __int__(self) -> int:
        return int(self.__value)  # type: ignore

    @_atomic_require_lock
    def __float__(self) -> float:
        return float(self.__value)  # type: ignore

    @_atomic_require_lock
    def __complex__(self) -> complex:
        return complex(self.__value)  # type: ignore

    @_atomic_require_context
    def __iadd__(self, value: int | float | complex) -> "AtomicNumber[NT]":
        self.__value = type(self.__value)(self.__value + value)  # type: ignore
        return self

    @_atomic_require_lock
    def __add__(self, value: int | float | complex) -> int | float | complex:
        return self.__value + value

    @_atomic_require_context
    def __isub__(self, value: NT) -> "AtomicNumber[NT]":
        self.__value = type(self.__value)(self.__value - value)
        return self

    @_atomic_require_lock
    def __sub__(self, value: int | float | complex) -> int | float | complex:
        return self.__value - value

    @_atomic_require_context
    def __ipow__(self, value: int | float | complex) -> "AtomicNumber[NT]":
        self.__value = type(self.__value)(
            self.__value ** value  # type: ignore
        )  # type: ignore
        return self

    @_atomic_require_lock
    def __pow__(self, value: int | float | complex) -> int | float | complex:
        return self.__value ** value

    @_atomic_require_context
    def __imul__(self, value: int | float | complex) -> "AtomicNumber[NT]":
        self.__value = type(self.__value)(self.__value * value)  # type: ignore
        return self

    @_atomic_require_lock
    def __mul__(self, value: int | float | complex) -> int | float | complex:
        return self.__value * value

    @_atomic_require_context
    def __itruediv__(self, value: int | float | complex) -> "AtomicNumber[NT]":
        self.__value = type(self.__value)(self.__value / value)  # type: ignore
        return self

    @_atomic_require_lock
    def __truediv__(
        self,
        value: int | float | complex
    ) -> int | float | complex:
        return self.__value / value

    @_atomic_require_context
    def __ifloordiv__(self, value: int | float) -> "AtomicNumber[NT]":
        self.__value = type(self.__value)(
            self.__value // value  # type: ignore
        )  # type: ignore
        return self

    @_atomic_require_lock
    def __floordiv__(self, value: int | float) -> int | float:
        return self.__value // value  # type: ignore


@final
class AtomicBool(_Atomic[bool]):
    """A thread-safe boolean whose updates are atomic."""

    __slots__ = {
        "__value": "The current value of the boolean."
    }

    def __init__(self, value: bool = False) -> None:
        """Create a new atomic boolean with given initial value."""
        super().__init__()
        self.__value = bool(value)

    @_atomic_require_lock
    def get_obj(self) -> bool:
        """Returns the current value of the boolean."""
        return self.__value

    @_atomic_require_context
    def set_obj(self, value: bool, /) -> None:
        """Sets the boolean to the given value."""
        self.__value = bool(value)

    @_atomic_require_context
    def get_and_set_value(self, value: bool) -> bool:
        """Sets the boolean to the given value and returns the old value."""
        old_value = self.__value
        self.__value = bool(value)
        return old_value

    @_atomic_require_context
    def compare_and_set_value(self, expected: bool, value: bool) -> bool:
        """
        Sets the boolean to the given value if the current value is equal to
        the expected value. Returns whether the value was set.
        """
        if self.__value == expected:
            self.__value = bool(value)
            return True
        return False

    @_atomic_require_lock
    def __bool__(self) -> bool:
        return self.__value

    @_atomic_require_context
    def __iand__(self, value: bool) -> "AtomicBool":
        self.__value &= bool(value)
        return self

    @_atomic_require_lock
    def __and__(self, value: bool) -> bool:
        return self.__value & value

    @_atomic_require_context
    def __ior__(self, value: bool) -> "AtomicBool":
        self.__value |= value
        return self

    @_atomic_require_lock
    def __or__(self, value: bool) -> bool:
        return self.__value | value

    @_atomic_require_context
    def __ixor__(self, value: bool) -> "AtomicBool":
        self.__value ^= value
        return self

    @_atomic_require_lock
    def __xor__(self, value: bool) -> bool:
        return self.__value ^ value


LT = TypeVar("LT")


class AtomicList(_Atomic[list[LT]], collections.abc.MutableSequence):
    """
    A thread-safe list whose updates are atomic.

    Updates to the list are only allowed within a context manager.
    """

    __slots__ = {
        "__list": "The wrapped list."
    }

    @overload
    def __init__(self) -> None:
        """Create a new empty atomic list."""
        ...

    @overload
    def __init__(self, __iterable: Iterable[LT], /) -> None:
        """Create a new atomic list with given initial value."""
        ...

    def __init__(  # type: ignore
        self,
        __iterable: Iterable[LT] | None = None, /
    ) -> None:
        super().__init__()
        self.__list: list[LT]
        if __iterable is not None:
            self.__list = list(__iterable)
        else:
            self.__list = []

    @_atomic_require_lock
    def get_obj(self) -> list[LT]:
        """Returns the current list."""
        return self.__list

    @_atomic_require_context
    def set_obj(self, value: Iterable[LT], /) -> None:
        """Sets the list to the given value."""
        self.__list = list(value)

    @_atomic_require_lock
    def __len__(self) -> int:
        return len(self.__list)

    @overload
    def __getitem__(self, key: int, /) -> LT:
        ...

    @overload
    def __getitem__(self, key: slice, /) -> "list[LT]":
        ...

    @_atomic_require_lock
    def __getitem__(  # type: ignore
        self,
        key: int | slice, /
    ) -> LT | "list[LT]":
        if isinstance(key, slice):
            return self.__list[key]
        else:
            return self.__list[key]

    @_atomic_require_lock
    def __contains__(self, value: object) -> bool:
        return value in self.__list

    @_atomic_require_lock
    def __iter__(self) -> Iterator[LT]:
        return iter(self.__list)

    @overload
    def __setitem__(self, key: int, value: LT, /) -> None:
        ...

    @overload
    def __setitem__(self, key: slice, value: Iterable[LT], /) -> None:
        ...

    @_atomic_require_context
    def __setitem__(  # type: ignore
        self,
        key: int | slice, value: LT | Iterable[LT], /
    ) -> None:
        self.__list[key] = value  # type: ignore

    @overload
    def __delitem__(self, key: int, /) -> None:
        ...

    @overload
    def __delitem__(self, key: slice, /) -> None:
        ...

    @_atomic_require_context
    def __delitem__(self, key: int | slice, /) -> None:
        del self.__list[key]

    @_atomic_require_context
    def __iadd__(self, value: Iterable[LT]) -> "AtomicList[LT]":
        self.__list += value
        return self

    @_atomic_require_lock
    def __add__(self, value: list[LT]) -> list[LT]:
        return self.__list + value

    @_atomic_require_context
    def __imul__(self, value: int) -> "AtomicList[LT]":
        self.__list *= value
        return self

    @_atomic_require_lock
    def __mul__(self, value: int) -> list[LT]:
        return self.__list * value

    @_atomic_require_lock
    def index(  # pylint: disable=arguments-differ
        self,
        value: LT,
        start: int = 0,
        stop: int = sys.maxsize, /
    ) -> int:
        super().index(value, start, stop)
        return self.__list.index(value, start, stop)
    index.__doc__ = list.index.__doc__

    @_atomic_require_lock
    def count(self, value: LT) -> int:
        return self.__list.count(value)
    count.__doc__ = list.count.__doc__

    @_atomic_require_context
    def append(self, value: LT) -> None:
        """Append an element to the end of the list."""
        self.__list.append(value)

    @_atomic_require_context
    def extend(self, values: Iterable[LT]) -> None:
        """Extend the list by appending elements from the iterable."""
        self.__list.extend(values)

    @_atomic_require_context
    def insert(self, index: int, value: LT) -> None:
        """Insert an element before the given index."""
        self.__list.insert(index, value)

    @_atomic_require_context
    def pop(self, index: int = -1) -> LT:
        return self.__list.pop(index)
    pop.__doc__ = list.pop.__doc__

    @_atomic_require_context
    def remove(self, value: LT) -> None:
        self.__list.remove(value)
    remove.__doc__ = list.remove.__doc__

    @_atomic_require_context
    def clear(self) -> None:
        """Remove all elements from the list."""
        self.__list.clear()

    @_atomic_require_context
    def reverse(self) -> None:
        """Reverse the elements of the list in-place."""
        self.__list.reverse()


KT = TypeVar("KT", bound=Hashable)
VT = TypeVar("VT")


class AtomicDict(_Atomic[dict[KT, VT]], collections.abc.MutableMapping):
    """
    A thread-safe dictionary whose updates are atomic.

    Updates to the dictionary are only allowed within a context manager.
    """

    __slots__ = {
        "__dict": "The wrapped dictionary."
    }

    def __init__(self, mapping: Mapping[KT, VT]) -> None:
        super().__init__()
        self.__dict: dict[KT, VT] = dict(mapping)

    @_atomic_require_lock
    def get_obj(self) -> dict[KT, VT]:
        """Returns the current dictionary."""
        return self.__dict

    @_atomic_require_context
    def set_obj(self, value: Mapping[KT, VT], /) -> None:
        """Sets the dictionary to the given value."""
        self.__dict = dict(value)

    @_atomic_require_lock
    def __getitem__(self, key: KT) -> VT:
        return self.__dict[key]

    @_atomic_require_context
    def __setitem__(self, key: KT, value: VT) -> None:
        self.__dict[key] = value

    @_atomic_require_context
    def __delitem__(self, key: KT) -> None:
        del self.__dict[key]

    @_atomic_require_lock
    def __iter__(self) -> Iterator[KT]:
        return iter(self.__dict)

    @_atomic_require_lock
    def __len__(self) -> int:
        return len(self.__dict)


ET = TypeVar("ET", bound=Hashable)


class AtomicSet(_Atomic[set[ET]], collections.abc.MutableSet):
    """
    A thread-safe set whose updates are atomic.

    Updates to the set are only allowed within a context manager.
    """

    __slots__ = {
        "__set": "The wrapped set."
    }

    def __init__(self, iterable: Iterable[ET]) -> None:
        super().__init__()
        self.__set: set[ET] = set(iterable)

    def __str__(self) -> str:
        return f"AtomicSet: {self.__set!s}"

    def __repr__(self) -> str:
        return f"AtomicSet({self.__set!r})"

    @_atomic_require_lock
    def get_obj(self) -> set[ET]:
        """Returns the current set."""
        return self.__set

    @_atomic_require_context
    def set_obj(self, value: Iterable[ET], /) -> None:
        """Sets the set to the given value."""
        self.__set = set(value)

    @_atomic_require_lock
    def __contains__(self, item: object) -> bool:
        return item in self.__set

    @_atomic_require_lock
    def __iter__(self) -> Iterator[ET]:
        return iter(self.__set)

    @_atomic_require_lock
    def __len__(self) -> int:
        return len(self.__set)

    @_atomic_require_context
    def add(self, value: ET) -> None:
        self.__set.add(value)

    @_atomic_require_context
    def discard(self, value: ET) -> None:
        self.__set.discard(value)


if __name__ == "__main__":
    atomic_object = AtomicList[int]([1, 2, 3])
    print(atomic_object)
    try:
        with atomic_object:
            atomic_object.append(4)
            atomic_object.append(5)
            atomic_object.append(6)
        print(atomic_object.get_obj())
        atomic_object.append(7)
        print(atomic_object.get_obj())
    except AloyAtomicObjectError:
        print("Error")
