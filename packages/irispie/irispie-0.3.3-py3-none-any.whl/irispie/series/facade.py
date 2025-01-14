"""
Time series facade
"""


#[
from __future__ import annotations

from numbers import Number
from collections.abc import (Iterable, Callable, )
from typing import (Self, TypeAlias, )
from types import (EllipsisType, )
import numpy as _np
import itertools as it_
import copy as _co

from ..user import views as _vi
from ..user import description as _ud
from ..dataman import dates as _da
from . import filters as _sg
from . import plotly as _sp
from . import conversion as _sc
from . import x13 as _sx
#]


FUNCTION_ADAPTATIONS = ["log", "exp", "sqrt", "maximum", "minimum"] + ["cumsum"] + ["maxi", "mini", "mean", "median"] + ["grow"]
_np.maxi = _np.max
_np.mini = _np.min


__all__ = [
    "Series", "shift",
    "diff", "difflog", "pct", "roc",
    "cum_diff", "cum_difflog", "cum_pct", "cum_roc",
] + FUNCTION_ADAPTATIONS


for n in FUNCTION_ADAPTATIONS:
    exec(
        f"def {n}(x, *args, **kwargs): "
        f"return x._{n}_(*args, **kwargs) if hasattr(x, '_{n}_') else _np.{n}(x, *args, **kwargs)"
    )
sum

Dates: TypeAlias = _da.Dater | Iterable[_da.Dater] | _da.Ranger | EllipsisType | None
Columns: TypeAlias = int | Iterable[int] | slice
Data: TypeAlias = Number | Iterable[Number] | tuple | _np.ndarray


def _get_date_positions(dates, base, num_periods):
    pos = list(_da.date_index(dates, base))
    min_pos = min((x for x in pos if x is not None), default=0)
    max_pos = max((x for x in pos if x is not None), default=0)
    add_before = max(-min_pos, 0)
    add_after = max(max_pos - num_periods, 0)
    pos_adjusted = [
        p + add_before if p is not None else None
        for p in pos
    ]
    return pos_adjusted, add_before, add_after


def _trim_decorate(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        return self._trim()
    return wrapper


class Series(
    _sg.HodrickPrescottMixin,
    _ud.DescriptionMixin,
    _sc.ConversionMixin,
    _sx.EggsThirteenMixin,
    _vi.SeriesViewMixin,
    _sp.PlotlyMixin,
):
    """
    """
    __slots__ = (
        "start_date", "data", "data_type",
        "_description", "_column_titles", "_user_data",
    )
    _numeric_format: str = "15g"
    _short_str_format: str = ">15"
    _date_str_format: str = ">12"
    _missing = _np.nan
    _missing_str: str = "·"
    _test_missing_period = staticmethod(lambda x: _np.all(_np.isnan(x)))

    def __init__(self, /, *args, **kwargs):
        num_columns = kwargs.get("num_columns", 1)
        self.data_type = kwargs.get("data_type", _np.float64)
        self._description = kwargs.get("description", "")
        self.reset(num_columns)

    def reset(self, /, num_columns=None, data_type=None, description=None, ):
        num_columns = num_columns if num_columns else self.num_columns
        data_type = data_type if data_type else self.data_type
        description = description if description else self._description
        self.start_date = None
        self.data = _np.full((0, num_columns), self._missing, dtype=data_type)
        self._description = str(description)
        self._column_titles = [""] * num_columns
        self._user_data = {}
        return self

    def _create_periods_of_missing_values(self, num_rows=0):
        return _np.full((num_rows, self.shape[1]), self._missing, dtype=self.data_type)

    @property
    def shape(self):
        return self.data.shape

    @property
    def num_columns(self):
        return self.data.shape[1]

    @property
    def range(self):
        return _da.Ranger(self.start_date, self.end_date) if self.start_date else []

    @property
    def end_date(self):
        return self.start_date + self.data.shape[0] - 1 if self.start_date else None

    @property
    def frequency(self):
        return self.start_date.frequency if self.start_date is not None else _da.Frequency.UNKNOWN

    @classmethod
    def from_dates_and_data(
        cls,
        dates: Iterable[_da.Dater],
        data: _np.ndarray | Iterable,
        /,
    ) -> Self:
        data = _conform_data(data)
        num_columns = data.shape[1] if hasattr(data, "shape") else 1
        self = cls(num_columns=num_columns)
        self.set_data(dates, data)
        return self

    from_dates_and_values = from_dates_and_data

    @classmethod
    def from_start_date_and_data(
        cls,
        start_date: _da.Dater,
        data: _np.ndarray | Iterable,
        /,
        **kwargs,
    ) -> Self:
        data = _conform_data(data, )
        num_columns = data.shape[1] if hasattr(data, "shape") else 1
        self = cls(num_columns=num_columns, **kwargs)
        self.start_date = start_date
        self.data = data
        return self._trim()

    @classmethod
    def from_func(
        cls,
        dates: Iterable[_da.Dater],
        func: Callable,
        /,
        **kwargs,
    ) -> Self:
        """
        """
        self = cls(**kwargs)
        dates = [ t for t in dates ]
        data = [ [ func() for j in range(self.num_columns) ] for i in range(len(dates)) ]
        data = _np.array(data, dtype=self.data_type)
        self.set_data(dates, data)
        return self

    @_trim_decorate
    def set_data(
        self,
        dates: Dates,
        data: Data | Series,
        columns: Columns = None,
        /,
    ) -> Self:
        dates = self._resolve_dates(dates)
        columns = self._resolve_columns(columns)
        if not self.start_date:
            self.start_date = next(iter(dates))
            self.data = self._create_periods_of_missing_values(1)
        pos, add_before, add_after = _get_date_positions(dates, self.start_date, self.shape[0]-1)
        self.data = self._create_expanded_data(add_before, add_after)
        if add_before:
            self.start_date -= add_before
        if hasattr(data, "get_data"):
            data = data.get_data(dates)
        if isinstance(data, _np.ndarray):
            self.data[pos, :] = data
            return
        if not isinstance(data, tuple):
            data = it_.repeat(data)
        for c, d in zip(columns, data):
            self.data[pos, c] = d
        return self

    def _get_data_and_recreate(
        self,
        *args,
    ) -> _np.ndarray:
        """
        """
        data, dates = self.get_data_and_resolved_dates(*args)
        num_columns = data.shape[1]
        new = Series(num_columns=num_columns, data_type=self.data_type)
        new.set_data(dates, data)
        return new

    def get_data_and_resolved_dates(
        self,
        dates: Dates,
        columns: Columns = None,
        /,
    ) -> _np.ndarray:
        """
        """
        dates = [ t for t in self._resolve_dates(dates) ]
        columns = self._resolve_columns(columns)
        base_date = self.start_date
        if not dates or not base_date:
            num_dates = len(set(dates))
            return self._create_periods_of_missing_values(num_dates)[:, columns], dates
        pos, add_before, add_after = _get_date_positions(dates, self.start_date, self.shape[0]-1)
        data = self._create_expanded_data(add_before, add_after)
        if not isinstance(pos, Iterable):
            pos = (pos, )
        return data[_np.ix_(pos, columns)], dates

    def get_data(
        self,
        *args,
    ) -> _np.ndarray:
        return self.get_data_and_resolved_dates(*args)[0]

    def get_data_column(
        self,
        dates: Dates,
        column: Number | None = None,
        /,
    ) -> _np.ndarray:
        """
        """
        column = column if column and column<self.data.shape[1] else 0
        return self.get_data(dates, column)

    def extract_columns(
        self,
        columns,
        /,
    ) -> None:
        if not isinstance(columns, Iterable):
            columns = (columns, )
        columns = [ c for c in columns ]
        self.data = self.data[:, columns]
        self.column_titles = [ self.column_titles[c] for c in columns ]

    def set_start_date(
        self,
        new_start_date: _da.Dater,
        /,
    ) -> Self:
        self.start_date = new_start_date
        return self

    def _resolve_dates(self, dates):
        if dates is None:
            return []
        if dates is Ellipsis:
            dates = _da.Ranger(None, None)
        if isinstance(dates, _da.ResolvableProtocol) and dates.needs_resolve:
            dates = dates.resolve(self)
        return dates

    def _resolve_columns(self, columns):
        if columns is None or columns is Ellipsis:
            columns = slice(None)
        if isinstance(columns, slice):
            columns = range(*columns.indices(self.num_columns))
        if not isinstance(columns, Iterable):
            columns = (columns, )
        return columns

    def __call__(self, *args):
        """
        Get data self[dates] or self[dates, columns]
        """
        return self.get_data(*args)

    def _shift(
        self,
        shift_by: int | str,
    ) -> None:
        match shift_by:
            case "yoy":
                self._shift_by_number(-self.frequency.value, )
            case "boy" | "soy":
                self._shift_to_soy()
            case "eopy":
                self._shift_to_eopy()
            case "tty":
                self._shift_to_tty()
            case _:
                self._shift_by_number(shift_by, )

    def _shift_by_number(self, shift_by: int, ) -> None:
        """
        Shift (lag, lead) start date by a number of periods
        """
        self.start_date = (
            self.start_date - shift_by 
            if self.start_date else self.start_date
        )

    def _shift_to_soy(self, ) -> None:
        new_data = self.get_data(
            t.create_soy()
            for t in self.range
        )
        self._replace_data(new_data, )

    def _shift_to_tty(self, ) -> None:
        new_data = self.get_data(
            t.create_tty()
            for t in self.range
        )
        self._replace_data(new_data, )

    def _shift_to_eopy(self, ) -> Self:
        new_data = self.get_data(
            t.create_eopy()
            for t in self.range
        )
        self._replace_data(new_data, )

    def __getitem__(self, index):
        """
        Create a new time series based on date retrieved by self[dates] or self[dates, columns]
        """
        if isinstance(index, int):
            new = _co.deepcopy(self)
            new._shift(index)
            return new
        if not isinstance(index, tuple):
            index = (index, None, )
        return self._get_data_and_recreate(*index)

    def __setitem__(self, index, data):
        """
        Set data self[dates] = ... or self[dates, columns] = ...
        """
        if not isinstance(index, tuple):
            index = (index, None, )
        return self.set_data(index[0], data, index[1])

    def hstack(self, *args):
        if not args:
            return _co.deepcopy(self)
        encompassing_range = _da.get_encompassing_range(self, *args)
        new_data = self.get_data(encompassing_range)
        add_data = (
            x.get_data(encompassing_range) if hasattr(x, "get_data") else _create_data_from_number(x, encompassing_range, self.data_type)
            for x in args
        )
        new_data = _np.hstack((new_data, *add_data))
        new = Series(num_columns=new_data.shape[1]);
        new.set_data(encompassing_range, new_data)
        return new

    def clip(
        self,
        new_start_date: _da.Dater | None,
        new_end_date: _da.Dater | None,
    ) -> None:
        if new_start_date is None or new_start_date < self.start_date:
            new_start_date = self.start_date
        if new_end_date is None or new_end_date > self.end_date:
            new_end_date = self.end_date
        if new_start_date == self.start_date and new_end_date == self.end_date:
            return
        self.start_date = new_start_date
        self.data = self.get_data(_da.Ranger(new_start_date, new_end_date))

    def is_empty(self, ) -> bool:
        return not self.data.size

    def empty(self, ) -> None:
        self.data = _np.empty((0, self.num_columns), dtype=self.data_type)

    def overlay_by_range(
        self,
        other: Self,
        /,
    ) -> Self:
        self._trim()
        other._trim()
        self.set_data(other.range, other.data, )
        return self

    def overlay(
        self,
        other: Self,
        /,
        method = "by_range",
    ) -> Self:
        return self._LAY_METHOD_RESOLUTION[method]["overlay"](self, other, )

    def underlay_by_range(
        self,
        other: Self,
        /,
    ) -> Self:
        """
        """
        self._trim()
        other._trim()
        self_range = self.range
        self_data = self.data
        #
        self.start_date = other.start_date
        enforce_columns = _np.zeros((1, self.data.shape[1]), dtype=self.data_type)
        self.data = enforce_columns + other.data
        self.set_data(self_range, self_data, )
        return self

    def underlay(
        self,
        other: Self,
        /,
        method = "by_range",
    ) -> Self:
        return self._LAY_METHOD_RESOLUTION[method]["underlay"](self, other, )

    _LAY_METHOD_RESOLUTION = {
        "by_range": {"overlay": overlay_by_range, "underlay": underlay_by_range},
    }

    def __or__(self, other):
        return self.hstack(other)

    def __lshift__(self, other):
        return _co.deepcopy(self).overlay_by_range(other, )

    def __rshift__(self, other):
        return _co.deepcopy(other).overlay_by_range(self, )

    def _trim(self):
        if self.data.size==0:
            return self.reset()
        num_leading = _get_num_leading_missing_rows(self.data, self._test_missing_period)
        if num_leading == self.data.shape[0]:
            return self.reset()
        num_trailing = _get_num_leading_missing_rows(self.data[::-1], self._test_missing_period)
        if not num_leading and not num_trailing:
            return self
        slice_from = num_leading if num_leading else None
        slice_to = -num_trailing if num_trailing else None
        self.data = self.data[slice(slice_from, slice_to), ...]
        if slice_from:
            self.start_date += int(slice_from)
        return self

    def _create_expanded_data(self, add_before, add_after):
        return _np.pad(
            self.data, ((add_before, add_after), (0, 0)),
            mode="constant", constant_values=self._missing
        )

    def _check_data_shape(self, data, /, ):
        if data.shape[1] != self.data.shape[1]:
            raise Exception("Time series data being assigned must preserve the number of columns")

    def __neg__(self):
        """
        -self
        """
        output = _co.deepcopy(self)
        output.data = -output.data
        return output

    def __pos__(self):
        """
        +self
        """
        return _co.deepcopy(self.copy)

    def __add__(self, other) -> Self|_np.ndarray:
        """
        self + other
        """
        arg = other.data if isinstance(other, type(self)) else other
        return self._binop(other, lambda x, y: x + y)

    def __radd__(self, other):
        """
        other + self
        """
        return self.apply(lambda data: data.__radd__(other))

    def __mul__(self, other) -> Self|_np.ndarray:
        """
        self + other
        """
        arg = other.data if isinstance(other, type(self)) else other
        return self._binop(other, lambda x, y: x * y)

    def __rmul__(self, other):
        """
        other + self
        """
        return self.apply(lambda data: data.__rmul__(other))

    def __sub__(self, other):
        """
        self - other
        """
        arg = other.data if isinstance(other, type(self)) else other
        return self._binop(other, lambda x, y: x - y)

    def __rsub__(self, other):
        """
        other - self
        """
        return self.apply(lambda data: data.__rsub__(other))

    def __pow__(self, other):
        """
        self ** other
        """
        # FIXME: 1 ** numpy.nan -> 1 !!!!!
        arg = other.data if isinstance(other, type(self)) else other
        return self._binop(other, lambda x, y: x ** y)

    def __rpow__(self, other):
        """
        other ** self
        """
        return self.apply(lambda data: data.__rpow__(other))

    def __truediv__(self, other):
        """
        self - other
        """
        arg = other.data if isinstance(other, type(self)) else other
        return self._binop(other, lambda x, y: x / y)

    def __rtruediv__(self, other):
        """
        other - self
        """
        return self.apply(lambda data: data.__rtruediv__(other))

    def __floordiv__(self, other):
        """
        self // other
        """
        return self._binop(other, lambda x, y: x // y)

    def __rfloordiv__(self, other):
        """
        other // self
        """
        return self.apply(lambda data: data.__rfloordiv__(other))

    def __mod__(self, other):
        """
        self % other
        """
        return self._binop(other, lambda x, y: x % y)

    def __rmod__(self, other, /, ):
        """
        other % self
        """
        return self.apply(lambda data: data.__rmod__(other))

    def apply(self, func, /, *args, **kwargs):
        new_data = func(self.data, *args, **kwargs)
        axis = kwargs.get("axis")
        if new_data.shape==self.data.shape:
            new = _co.deepcopy(self)
            new.data = new_data
            return new._trim()
        elif (axis is None or axis==1) and new_data.shape==(self.data.shape[0],):
            new = _co.deepcopy(self)
            new.data = new_data.reshape(self.data.shape[0], 1)
            return new._trim()
        elif axis is None and new_data.shape==():
            return new_data
        elif axis==0 and new_data.shape==(self.data.shape[1],):
            return new_data
        else:
            raise Exception("Function applied on a time series resulted in a data array with an unexpected shape")

    def _binop(self, other, func, /, ):
        if not isinstance(other, type(self)):
            unop_func = lambda data: func(data, other)
            return apply(self, unop_func)
        encompassing_range = _da.get_encompassing_range(self, other)
        self_data = self.get_data(encompassing_range)
        other_data = other.get_data(encompassing_range)
        new = Series()
        new.start_date = encompassing_range[0]
        new.data = func(self_data, other_data)
        new._trim()
        return new

    def _replace_data(self, new_data, /, ) -> None:
        self.data = new_data
        self._trim()

    def copy(self, /, ) -> Self:
        return _co.deepcopy(self, )

    for n in ["log", "exp", "sqrt", "maximum", "minimum"]:
        exec(f"def {n}(self, *args, **kwargs, ): return self._replace_data(_np.{n}(self.data, *args, **kwargs, ), )")
        exec(f"def _{n}_(self, *args, **kwargs, ): return self.apply(_np.{n}, *args, **kwargs, )")

    for n in ["cumsum"]:
        exec(f"def {n}(self): return self._replace_data(_np.{n}(self.data, axis=0, ), )")

    for n in ["maxi", "mini", "mean", "median"]:
        exec(f"def _{n}_(self, *args, **kwargs): return self.apply(_np.{n}, *args, **kwargs, )")


def _get_num_leading_missing_rows(data, test_missing_period, /, ):
    try:
        num = next(
            i for i, period_data in enumerate(data) 
            if not test_missing_period(period_data)
        )
    except StopIteration:
        num = data.shape[0]
    return num


# def apply(x, func: Callable, /, *args, **kwargs) -> object:
    # if isinstance(x, Series):
        # return x.apply(func, *args, **kwargs)
    # else:
        # return func(x, *args, **kwargs)

def hstack(first, *args) -> Self:
    return first.hstack(*args)


def _create_data_from_number(
    number: Number,
    range: _da.Ranger,
    data_type: type,
    /,
) -> _np.ndarray:
    return _np.full((len(range), 1), number, dtype=data_type)


def shift(x, by=-1, ) -> Series:
    new = _co.deepcopy(x)
    new._shift(by)
    return new


def _negative_by_decorator(func):
    def wrapper(x, *args, **kwargs, ):
        if len(args) > 0:
            by = args[0]
            if not isinstance(by, str) and (int(by) != by or by >= 0):
                raise Exception("Time shift must be a negative integer")
        return func(x, *args, **kwargs, )
    return wrapper


@_negative_by_decorator
def diff(x, by=-1, /, ) -> Series:
    return x - shift(x, by)


@_negative_by_decorator
def cum_diff(dx, by=-1, /, initial=0, range=_da.Ranger(), ) -> Series:
    return _cumulate(dx, by, "diff", initial, range, )


@_negative_by_decorator
def difflog(x, by=-1, /, ) -> Series:
    return log(x) - log(shift(x, by))


@_negative_by_decorator
def cum_difflog(dx, by=-1, /, initial=1, range=_da.Ranger(), ) -> Series:
    return _cumulate(dx, by, "difflog", initial, range, )


@_negative_by_decorator
def pct(x, shift=-1, /, ) -> Series:
    return 100*(x/shift(x, by) - 1)


@_negative_by_decorator
def cum_pct(dx, by=-1, /, initial=1, range=_da.Ranger(), ) -> Series:
    return _cumulate(dx, by, "pct", initial, range, )


@_negative_by_decorator
def roc(x, shift=-1, /, ) -> Series:
    return x/shift(x, by)


@_negative_by_decorator
def cum_roc(roc, by=-1, /, initial=1, range=_da.Ranger(), ) -> Series | None:
    return _cumulate(roc, by, "roc", initial, range, )


_CUMULATIVE_FUNCTIONS = {
    "diff": {
        "forward": lambda x_past, change_curr: x_past + change_curr,
        "backward": lambda x_future, change_future: x_future - change_future,
    },
    "difflog": {
        "forward": lambda x_past, change_curr: x_past * exp(change_curr),
        "backward": lambda x_future, change_future: x_future / exp(change_future),
    },
    "pct": {
        "forward": lambda x_past, change_curr: x_past * (1 + change_curr/100),
        "backward": lambda x_future, change_future: x_future / (1 + change_future/100),
    },
    "roc": {
        "forward": lambda x_past, change_curr: x_past * change_curr,
        "backward": lambda x_future, change_future: x_future / change_future,
    },
}


def _cumulate(dx, by, func, initial, range, /, ) -> Series:
    direction = range.direction
    cum_func = _CUMULATIVE_FUNCTIONS[func][direction]
    new = Series(num_columns=dx.num_columns, data_type=dx.data_type, )
    match direction:
        case "forward":
            _cumulate_forward(new, dx, by, cum_func, initial, range, )
        case "backward":
            _cumulate_backward(new, dx, by, cum_func, initial, range, )
    return new._trim()


def _cumulate_forward(new, dx, by, cum_func, initial, range, /, ) -> None:
    range = range.resolve(dx)
    shifted_range = tuple(t.shift(by) for t in range)
    initial_range = _da.Ranger(min(shifted_range), range.end_date, )
    new.set_data(initial_range, initial)
    for t, sh in zip(range, shifted_range):
        new_data = cum_func(new.get_data(sh, ), dx.get_data(t, ), )
        new.set_data(t, new_data)


def _cumulate_backward(new, dx, by, cum_func, initial, shifted_backward_range, /, ) -> None:
    dx_range_shifted = _da.Ranger(dx.start_date, dx.end_date, -1, )
    dx_range_shifted.shift(by)
    shifted_backward_range = shifted_backward_range.resolve(dx_range_shifted)
    backward_range = shifted_backward_range.copy()
    backward_range.shift(-by)
    initial_range = _da.Ranger(min(shifted_backward_range), backward_range.start_date)
    new.set_data(initial_range, initial)
    for t, sh in zip(backward_range, shifted_backward_range):
        new_data = cum_func(new.get_data(t, ), dx.get_data(t, ), )
        new.set_data(sh, new_data)


def _conform_data(data, /, ) -> _np.ndarray:
    if not isinstance(data, _np.ndarray, ):
        data = _np.array(data, dtype=float, ndmin=2, ).T
    return data

