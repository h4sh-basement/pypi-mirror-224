"""
Dates, date ranges, and date frequencies
"""


#[
from __future__ import annotations
import re as _re
import datetime as _dt
import enum as _en
import functools as _ft
from typing import (Union, Self, Any, Protocol, TypeAlias, runtime_checkable, )
from collections.abc import (Iterable, Callable, )
from numbers import (Number, )

from ..user import copy as _cp
#]


__all__ = [
    "Frequency",
    "yy", "hh", "qq", "mm", "dd", "ii",
    "Ranger", "start", "end",
    "dater_from_sdmx_string",
    "daters_from_sdmx_strings",
    "dater_from_iso_string",
    "daters_from_iso_strings",
]


class Frequency(_en.IntEnum):
    """
    Enumeration of date frequencies
    """
    #[
    INTEGER = 0
    YEARLY = 1
    HALFYEARLY = 2
    QUARTERLY = 4
    MONTHLY = 12
    WEEKLY = 52
    DAILY = 365
    UNKNOWN = -1

    @classmethod
    def from_letter(cls, letter: str, /, ) -> Frequency:
        """
        """
        return next(
            x for x in cls
            if x.name.startswith(letter.upper()) and x is not cls.UNKNOWN
        )

    @property
    def letter(self, /, ) -> str:
        return self.name[0] if self is not self.UNKNOWN else "?"

    @property
    def plotly_format(self, /, ) -> str:
        return PLOTLY_FORMATS[self]

    @property
    def is_regular(self, /, ) -> bool:
        return self in [self.YEARLY, self.HALFYEARLY, self.QUARTERLY, self.MONTHLY]

    def __str__(self, /, ) -> str:
        return self.name
    #]


PLOTLY_FORMATS = {
    Frequency.INTEGER: None,
    Frequency.YEARLY: "%Y",
    Frequency.HALFYEARLY: "%Y-%m",
    Frequency.QUARTERLY: "%Y-Q%q",
    Frequency.MONTHLY: "%Y-%m",
    Frequency.WEEKLY: "%Y-%W",
    Frequency.DAILY: "%Y-%m-%d",
}


BASE_YEAR = 2020


@runtime_checkable
class ResolutionContextProtocol(Protocol, ):
    """
    Context protocol for contextual date resolution
    """
    start_date = ...
    end_date = ...


@runtime_checkable
class ResolvableProtocol(Protocol, ):
    """
    Contextual date protocol
    """
    needs_resolve = ...
    def resolve(self, context: ResolutionContextProtocol) -> Any: ...


def _check_daters(first, second) -> None:
    if type(first) is not type(second):
        raise Exception("Dates must be the same date frequency")


def _check_daters_decorate(func: Callable, ) -> Callable:
    def wrapper(*args, **kwargs):
        _check_daters(args[0], args[1], )
        return func(*args, **kwargs, )
    return wrapper


def _check_offset(offset, ) -> None:
    if not isinstance(offset, int, ):
        raise Exception("Date offset must be an integer")


def _check_offset_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        _check_offset(args[1])
        return func(*args, **kwargs)
    return wrapper


def _remove_blanks(func: Callable,) -> Callable:
    def wrapper(*args, **kwargs, ):
        return func(*args, **kwargs, ).replace(" ", "", )
    return wrapper


class RangeableMixin:
    #[
    def __rshift__(self, end_date: Self) -> Ranger:
        """
        """
        return Ranger(self, end_date, 1)

    def __lshift__(self, start_date: Self) -> Ranger:
        """
        """
        return Ranger(start_date, self, -1) 
    #]


class IsoMixin:
    #[
    def to_iso_string(
        self,
        /,
        position: Literal["start"] | Literal["center"] | Literal["end"] = "start",
    ) -> str:
        year, month, day = self.to_ymd(position=position, )
        return f"{year:04g}-{month:02g}-{day:02g}"

    @classmethod
    def from_iso_string(cls: type, iso_string: str, ) -> Self:
        year, month, day = iso_string.split("-", )
        return cls.from_ymd(int(year), int(month), int(day), )

    to_plotly_date = _ft.partialmethod(to_iso_string, position="center")
    #]


class Dater(
    RangeableMixin,
    _cp.CopyMixin,
):
    """
    """
    #[
    frequency = None
    needs_resolve = False

    def __init__(self, serial=0) -> None:
        self.serial = int(serial)

    def get_distance_from_origin(self) -> int:
        return self.serial - self.origin

    def resolve(self, context: ResolutionContextProtocol) -> Self:
        return self

    def __bool__(self) -> bool:
        return not self.needs_resolve

    def __len__(self):
        return 1

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.to_sdmx_string()

    _databank_repr = __str__

    def __format__(self, *args) -> str:
        str_format = args[0] if args else ""
        return ("{date_str:"+str_format+"}").format(date_str=self.__str__())

    def __iter__(self) -> Iterable[Self]:
        yield self

    def _get_hash_key(self, /, ) -> tuple[int, int]:
        return (int(self.serial), int(self.frequency), )

    def __hash__(self, /, ) -> int:
        return hash(self._get_hash_key(), )

    @_check_offset_decorator
    def __add__(self, other: int) -> Self:
        return type(self)(self.serial + int(other))

    __radd__ = __add__

    def __sub__(self, other: Union[Self, int]) -> Union[Self, int]:
        if isinstance(other, Dater):
            return self._sub_dater(other)
        else:
            return self.__add__(-int(other))

    @_check_daters_decorate
    def _sub_dater(self, other: Self) -> int:
        return self.serial - other.serial

    def __index__(self):
        return self.serial

    @_check_daters_decorate
    def __eq__(self, other) -> bool:
        return self.serial == other.serial

    @_check_daters_decorate
    def __ne__(self, other) -> bool:
        return self.serial != other.serial

    @_check_daters_decorate
    def __lt__(self, other) -> bool:
        return self.serial < other.serial

    @_check_daters_decorate
    def __le__(self, other) -> bool:
        return self.serial <= other.serial

    @_check_daters_decorate
    def __gt__(self, other) -> bool:
        return self.serial > other.serial

    @_check_daters_decorate
    def __ge__(self, other) -> bool:
        return self.serial >= other.serial
    #]


class IntegerDater(Dater, ):
    #[
    frequency = Frequency.INTEGER
    needs_resolve = False
    origin = 0

    @classmethod
    def from_sdmx_string(cls, sdmx_string: str) -> IntegerDater:
        sdmx_string = sdmx_string.strip().removeprefix("(", "").removesuffix(")")
        return cls(int(sdmx_string))

    def to_sdmx_string(self) -> str:
        return f"({self.serial})"

    def to_plotly_date(self) -> str:
        return str(self.serial)

    def __repr__(self) -> str:
        return f"ii({self.serial})"

    def to_plotly_date(self):
        return self.serial
    #]


class DailyDater(Dater, IsoMixin):
    #[
    frequency: Frequency = Frequency.DAILY
    needs_resolve = False
    origin = _dt.date(BASE_YEAR, 1, 1).toordinal()

    @classmethod
    def from_ymd(cls: type, year: int, month: int=1, day: int=1) -> Self:
        serial = _dt.date(year, month, day).toordinal()
        return cls(serial)

    @classmethod
    def from_year_period(cls, year: int, period: int) -> Self:
        boy_serial = _dt.date(year, 1, 1).toordinal()
        serial = boy_serial + int(period) - 1
        return cls(serial)

    @classmethod
    def from_sdmx_string(cls, sdmx_string: str) -> DailyDater:
        year, month, day, *_ = sdmx_string.split("-")
        return cls.from_ymd(int(year), int(month), int(day))

    def to_sdmx_string(self, /, **kwargs) -> str:
        year, month, day = self.to_ymd()
        return f"{year:04g}-{month:02g}-{day:02g}"

    def to_year_period(self) -> tuple[int, int]:
        boy_serial = _dt.date(_dt.date.fromordinal(self.serial).year, 1, 1)
        per = self.serial - boy_serial + 1
        year = _dt.date.fromordinal(self.serial).year
        return year, per

    def to_ymd(self, /, **kwargs) -> tuple[int, int, int]:
        py_date = _dt.date.fromordinal(self.serial)
        return py_date.year, py_date.month, py_date.day

    def get_year(self, /, ) -> int:
        return _dt.date.fromordinal(self.serial).year

    @_remove_blanks
    def __repr__(self) -> str:
        return f"dd{self.to_ymd()}"

    def to_start_of_year(self, ) -> Self:
        year = self.get_year()
        serial = _dt.date(year, 1, 1).toordinal()
        return type(self)(serial)

    def to_end_of_year(self, ) -> Self:
        year = self.get_year()
        serial = _dt.date(year, 12, 31).toordinal()
        return type(self)(serial)

    def to_end_of_previous_year(self, ) -> Self:
        year = self.get_year()
        serial = _dt.date(year-1, 12, 31).toordinal()
        return type(self)(serial)

    def to_daily(self, /, **kwargs, ) -> Self:
        return self
    #]


def _serial_from_ypf(year: int, per: int, freq: int) -> int:
    return int(year)*int(freq) + int(per) - 1


class RegularDaterMixin(IsoMixin, ):
    #[
    @classmethod
    def from_year_period(
            cls: type,
            year: int,
            per: int | str = 1,
        ) -> Self:
        per = per if per != "end" else cls.frequency.value
        new_serial = _serial_from_ypf(year, per, cls.frequency.value)
        return cls(new_serial)

    @classmethod
    def from_ymd(cls, year: int, month: int=1, day: int=1, ) -> YearlyDater:
        return cls.from_year_period(year, cls.month_to_period(month, ), )

    def to_year_period(self) -> tuple[int, int]:
        return self.serial//self.frequency.value, self.serial%self.frequency.value+1

    def get_year(self) -> int:
        return self.to_year_period()[0]

    def to_ymd(
        self, 
        /,
        position: Literal["start"] | Literal["center"] | Literal["end"] = "center",
    ) -> tuple[int, int, int]:
        year, per = self.to_year_period()
        return year, *self.month_day_resolution[position][per]

    def __str__(self) -> str:
        year, per = self.to_year_period()
        letter = self.frequency.letter
        return self.frequency.sdmx_format.format(year=year, per=per, letter=letter)

    def to_start_of_year(self, ) -> Self:
        year, *_ = self.to_year_period()
        return self.from_year_period(year, 1)

    def to_end_of_year(self, ) -> Self:
        year, *_ = self.to_year_period()
        return self.from_year_period(year, self.frequency.value)

    def to_end_of_previous_year(self, ) -> Self:
        year, *_ = self.to_year_period()
        return self.from_year_period(year-1, self.frequency.value)

    def to_daily(
        self,
        /,
        position: Literal["start"] | Literal["center"] | Literal["end"] = "center"
    ) -> DailyDater:
        return DailyDater.from_ymd(*self.to_ymd(position=position))
    #]


class YearlyDater(Dater, RegularDaterMixin, ): 
    #[
    frequency: Frequency = Frequency.YEARLY
    needs_resolve: bool = False
    origin = _serial_from_ypf(BASE_YEAR, 1, Frequency.YEARLY)
    month_day_resolution = {
        "start": {1: (1, 1)},
        "center": {1: (6, 30)},
        "end": {1: (12, 31)},
    }

    @classmethod
    def from_sdmx_string(cls, sdmx_string: str) -> YearlyDater:
        return cls(int(sdmx_string))

    def to_sdmx_string(self) -> str:
        return f"{self.get_year():04g}"

    @_remove_blanks
    def __repr__(self) -> str: return f"yy({self.get_year()})"

    @staticmethod
    def month_to_period(month: int, ) -> int:
        return 1
    #]


class HalfyearlyDater(Dater, RegularDaterMixin, ):
    #[
    frequency: Frequency = Frequency.HALFYEARLY
    needs_resolve: bool = False
    origin = _serial_from_ypf(BASE_YEAR, 1, Frequency.HALFYEARLY)
    month_day_resolution = {
        "start": {1: (1, 1), 2: (7, 1)},
        "center": {1: (3, 15), 2: (9, 15)},
        "end": {1: (6, 30), 2: (12, 31)}
    }

    @classmethod
    def from_sdmx_string(cls, sdmx_string: str) -> HalfyearlyDater:
        year, halfyear = sdmx_string.split("-H")
        return cls.from_year_period(int(year), int(halfyear))

    def to_sdmx_string(self) -> str:
        year, per = self.to_year_period()
        return f"{year:04g}-{self.frequency.letter}{per:1g}"

    @_remove_blanks
    def __repr__(self) -> str: return f"hh{self.to_year_period()}"

    def to_ymd(
        self, 
        /,
        position: Literal["start"] | Literal["center"] | Literal["end"] = "center",
    ) -> tuple[int, int, int]:
        year, per = self.to_year_period()
        return (
            year,
            *{"start": (1, 1), "center": (6, 3), "end": (12, 31)}[position],
        )

    def get_month(
        self,
        /,
        position: Literal["start"] | Literal["center"] | Literal["end"] = "center",
    ) -> int:
        _, per = self.to_year_period()
        return month_resolution[position][per]

    @staticmethod
    def month_to_period(month: int, ) -> int:
        return 1+((month-1)//6)
    #]


class QuarterlyDater(Dater, RegularDaterMixin, ):
    frequency: Frequency = Frequency.QUARTERLY
    needs_resolve: bool = False
    origin = _serial_from_ypf(BASE_YEAR, 1, Frequency.QUARTERLY)
    month_day_resolution = {
        "start": {1: (1, 1), 2: (4, 1), 3: (7, 1), 4: (10, 1)},
        "center": {1: (2, 15), 2: (5, 15), 3: (8, 15), 4: (11, 15)},
        "end": {1: (3, 30), 2: (6, 31), 3: (9, 31), 4: (12, 31)},
    }

    @classmethod
    def from_sdmx_string(cls, sdmx_string: str) -> QuarterlyDater:
        year, quarter = sdmx_string.split("-Q")
        return cls.from_year_period(int(year), int(quarter))

    def to_sdmx_string(self) -> str:
        year, per = self.to_year_period()
        return f"{year:04g}-{self.frequency.letter}{per:1g}"

    @_remove_blanks
    def __repr__(self) -> str: return f"qq{self.to_year_period()}"

    @staticmethod
    def month_to_period(month: int, ) -> int:
        return 1+((month-1)//3)


class MonthlyDater(Dater, RegularDaterMixin, ):
    #[
    frequency: Frequency = Frequency.MONTHLY
    needs_resolve: bool = False
    origin = _serial_from_ypf(BASE_YEAR, 1, Frequency.MONTHLY)
    month_day_resolution = {
        "start": {1: (1, 1), 2: (2, 1), 3: (2, 1), 4: (4, 1), 5: (5, 1), 6: (6, 1), 7: (7, 1), 8: (8, 1), 9: (9, 1), 10: (10, 1), 11: (11, 1), 12: (12, 1)},
        "center": {1: (1, 15), 2: (2, 15), 3: (2, 15), 4: (4, 15), 5: (5, 15), 6: (6, 15), 7: (7, 15), 8: (8, 15), 9: (9, 15), 10: (10, 15), 11: (11, 15), 12: (12, 15)},
        "end": {1: (1, 31), 2: (2, 28), 3: (2, 31), 4: (4, 30), 5: (5, 31), 6: (6, 30), 7: (7, 31), 8: (8, 31), 9: (9, 30), 10: (10, 31), 11: (11, 30), 12: (12, 31)},
    }

    @classmethod
    def from_sdmx_string(cls, sdmx_string: str) -> MonthlyDater:
        year, month = sdmx_string.split("-")
        return cls.from_year_period(int(year), int(month))

    def to_sdmx_string(self) -> str:
        year, per = self.to_year_period()
        return f"{year:04g}-{per:02g}"

    @_remove_blanks
    def __repr__(self) -> str: return f"mm{self.to_year_period()}"

    @staticmethod
    def month_to_period(month: int, ) -> int:
        return month
    #]


yy = YearlyDater.from_year_period

hh = HalfyearlyDater.from_year_period

qq = QuarterlyDater.from_year_period

mm = MonthlyDater.from_year_period

ii = IntegerDater




def dd(year: int, month: int | ellipsis, day: int) -> DailyDater:
    if month is Ellipsis:
        return DailyDater.from_year_period(year, day)
    else:
        return DailyDater.from_ymd(year, month, day)


class Ranger():
    #[
    def __init__(
        self, 
        start_date: Dater|None =None,
        end_date: Dater|None =None,
        step: int=1,
        /
    ) -> None:
        """
        Date range constructor
        """
        start_date = resolve_dater_or_integer(start_date)
        end_date = resolve_dater_or_integer(end_date)
        self._start_date = start_date if start_date is not None else start
        self._end_date = end_date if end_date is not None else end
        self._step = step
        self.needs_resolve = self._start_date.needs_resolve or self._end_date.needs_resolve
        if not self.needs_resolve:
            _check_daters(start_date, end_date)

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def step(self):
        return self._step

    @property
    def _class(self):
        return type(self._start_date) if not self.needs_resolve else None

    @property
    def _serials(self) -> range|None:
        return range(self._start_date.serial, self._end_date.serial+_sign(self._step), self._step) if not self.needs_resolve else None

    # @property
    # def needs_resolve(self) -> bool:
        # return bool(self._start_date and self._end_date)

    @property
    def frequency(self) -> Frequency:
        return self._class.frequency

    def to_plotly_dates(self) -> Iterable[str]:
        return [t.to_plotly_date() for t in self]

    def __len__(self) -> int|None:
        return len(self._serials) if not self.needs_resolve else None

    def __str__(self) -> str:
        step_str = f", {self._step}" if self._step!=1 else ""
        start_date_str = self._start_date.__str__()
        end_date_str = self._end_date.__str__()
        return f"Ranger({start_date_str}, {end_date_str}{step_str})"

    def __repr__(self) -> str:
        step_rep = f", {self._step}" if self._step!=1 else ""
        start_date_rep = self._start_date.__repr__()
        end_date_rep = self._end_date.__repr__()
        return f"Ranger({start_date_rep}, {end_date_rep}{step_rep})"

    def __add__(self, offset: int) -> range:
        return Ranger(self._start_date+offset, self._end_date+offset, self._step)

    __radd__ = __add__

    def __sub__(self, offset: Union[Dater, int]) -> Union[range, Self]:
        if isinstance(offset, Dater):
            return range(self._start_date-offset, self._end_date-offset, self._step) if not self.needs_resolve else None
        else:
            return Ranger(self._start_date-offset, self._end_date-offset, self._step)

    def __rsub__(self, ather: Dater) -> range|None:
        if isinstance(other, Dater):
            return range(other-self._start_date, other-self._end_date, -self._step) if not self.needs_resolve else None
        else:
            return None

    def __iter__(self) -> Iterable:
        return (self._class(x) for x in self._serials) if not self.needs_resolve else None

    def __getitem__(self, i: int) -> Dater|None:
        return self._class(self._serials[i]) if not self.needs_resolve else None

    def resolve(self, context: ResolutionContextProtocol) -> Self:
        resolved_start_date = self._start_date if self._start_date else self._start_date.resolve(context)
        resolved_end_date = self._end_date if self._end_date else self._end_date.resolve(context)
        return Ranger(resolved_start_date, resolved_end_date, self._step)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def __eq__(self, other: Self) -> bool:
        return self._start_date==other._start_date and self._end_date==other._end_date and self._step==other._step

    def __bool__(self) -> bool:
        return not self.needs_resolve
    #]


def _sign(x: Number) -> int:
    return 1 if x>0 else (0 if x==0 else -1)


def date_index(dates: Iterable[Dater], base: Dater) -> Iterable[int]:
    return (x-base for x in dates)



class ContextualDater(Dater, RangeableMixin):
    """
    Dates with context dependent resolution
    """
    #[
    needs_resolve = True

    def __init__(self, resolve_from: str, offset: int=0) -> None:
        self._resolve_from = resolve_from
        self._offset = offset

    def __add__(self, offset: int) -> None:
        return type(self)(self._resolve_from, self._offset+offset)

    def __sub__(self, offset: int) -> None:
        return type(self)(self._resolve_from, self._offset-offset)

    def __str__(self) -> str:
        return "<>." + self._resolve_from + (f"{self._offset:+g}" if self._offset else "")

    def __repr__(self) -> str:
        return self.__str__()

    def __bool__(self) -> bool:
        return False

    def resolve(self, context: ResolutionContextProtocol) -> Dater:
        return getattr(context, self._resolve_from) + self._offset
    #]


start = ContextualDater("start_date")
end = ContextualDater("end_date")


def resolve_dater_or_integer(input_date: Any) -> Dater:
    """
    Convert non-dater to integer dater
    """
    if isinstance(input_date, Number):
        input_date = IntegerDater(int(input_date))
    return input_date


DATER_CLASS_FROM_FREQUENCY_RESOLUTION = {
    Frequency.INTEGER: IntegerDater,
    Frequency.YEARLY: YearlyDater,
    Frequency.HALFYEARLY: HalfyearlyDater,
    Frequency.QUARTERLY: QuarterlyDater,
    Frequency.MONTHLY: MonthlyDater,
    Frequency.DAILY: DailyDater,
}


def dater_from_sdmx_string(freq: Frequency, sdmx_string: str, ) -> Dater:
    """
    """
    return DATER_CLASS_FROM_FREQUENCY_RESOLUTION[freq].from_sdmx_string(sdmx_string)


def daters_from_sdmx_strings(freq: Frequency, sdmx_strings: Iterable[str], ) -> Iterable[Dater]:
    """
    """
    return (DATER_CLASS_FROM_FREQUENCY_RESOLUTION[freq].from_sdmx_string(x) for x in sdmx_strings)


def dater_from_iso_string(freq: Frequency, iso_string: str, ) -> Dater:
    """
    """
    return DATER_CLASS_FROM_FREQUENCY_RESOLUTION[freq].from_iso_string(iso_string)


def daters_from_iso_strings(freq: Frequency, iso_strings: Iterable[str], ) -> Iterable[Dater]:
    """
    """
    return (DATER_CLASS_FROM_FREQUENCY_RESOLUTION[freq].from_iso_string(x) for x in iso_strings)


def dater_from_ymd(freq: Frequency, *args, ) -> Dater:
    """
    """
    return DATER_CLASS_FROM_FREQUENCY_RESOLUTION[freq].from_ymd(*args, )


_FREQUENCY_FROM_STRING_RESOLUTION = {
    "I": Frequency.INTEGER,
    "Y": Frequency.YEARLY,
    "H": Frequency.HALFYEARLY,
    "Q": Frequency.QUARTERLY,
    "M": Frequency.MONTHLY,
    "W": Frequency.WEEKLY,
    "D": Frequency.DAILY,
}


def frequency_from_string(text: str) -> Frequency:
    """
    """
    first_letter_match = _re.search("[A-Z]", text.upper() + "X")
    return _FREQUENCY_FROM_STRING_RESOLUTION.get(first_letter_match.group(0), Frequency.UNKNOWN)


def get_encompassing_range(*args: ResolutionContextProtocol, ) -> Ranger:
    start_dates = [x.start_date for x in args if hasattr(x, "start_date") and x.start_date]
    end_dates = [x.end_date for x in args if hasattr(x, "end_date") and x.end_date]
    start_date = min(start_dates) if start_dates else None
    end_date = max(end_dates) if end_dates else None
    return Ranger(start_date, end_date)

