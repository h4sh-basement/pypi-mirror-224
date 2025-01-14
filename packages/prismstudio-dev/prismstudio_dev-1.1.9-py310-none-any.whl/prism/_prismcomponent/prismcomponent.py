import copy
import numbers
import inspect
import requests
import uuid
from abc import ABC, abstractmethod
from functools import wraps
from typing import Union

from .._prismcomponent.abstract_prismcomponent import _AbstractPrismComponent
from .._common.config import URL_DATAQUERIES
from .._common.const import *
from .._core._req_builder import _taskquery
from .._utils import _validate_args, _authentication
from .._utils.exceptions import PrismAuthError, PrismResponseError, PrismTypeError, PrismValueError


def binary_operation(func):
    @wraps(func)
    def wrapper(obj, other):
        func(obj, other)
        ops = FUNCTIONS.get(func.__name__)
        s_op = ops.get("op")

        if other is None:
            raise PrismTypeError(f"{s_op} missing 1 required positional argument")

        if isinstance(other, numbers.Real) or isinstance(other, str):
            other = SPECIALVALUEMAP.get(other, other)
            other_node = _PrismValue(data=other)
        elif isinstance(other, _PrismComponent):
            other_node = other
        elif (obj._component_name == "SecurityMaster") & isinstance(other, str):
            other = SPECIALVALUEMAP.get(other, other)
            other_node = _PrismValue(data=other)
        else:
            raise PrismTypeError(f"unsupported operand type(s) for {s_op}: {type(obj)}, {type(other)}")

        component_name = func.__name__
        component_args = {}
        ret = _functioncomponent_builder(component_name, component_args, obj, other_node)
        return ret

    return wrapper


def get_default_args(func):
    signature = inspect.signature(func)
    return {k: v.default for k, v in signature.parameters.items() if v.default is not inspect.Parameter.empty}


def operation(func):
    @wraps(func)
    def wrapper(obj, *args, **kwargs):
        func(obj, *args, **kwargs)
        vars = func.__code__.co_varnames[1:]
        component_name = func.__name__
        component_args = dict(zip(vars[: len(args)], args))
        component_args_copy = get_default_args(func)
        component_args_copy.update(dict(kwargs))
        component_args_copy.update(component_args)
        ret = _functioncomponent_builder(component_name, component_args_copy, obj)
        return ret

    return wrapper


def n_period_operation(func):
    @wraps(func)
    def wrapper(obj, n, *args, **kwargs):
        if not issubclass(type(n), int):
            raise PrismTypeError(f"Type of n is {type(n)} and not {int}")
        if "shift" in func.__name__:
            if n < 1:
                raise PrismValueError("n must be a positive integer")
        return func(obj, n, *args, **kwargs)

    return wrapper


def cross_sectional_operation(func):
    return operation(func)


def group_operation(func):
    @wraps(func)
    def wrapper(obj, other, *args, **kwargs):
        func(obj, other, *args, **kwargs)
        if other is None:
            raise PrismTypeError("Operation needs two inputs.")
        vars = func.__code__.co_varnames[2:]
        component_name = func.__name__
        component_args = dict(zip(vars[: len(args)], args))
        component_args.update(dict(kwargs))
        ret = _functioncomponent_builder(component_name, component_args, obj, other)
        return ret

    return wrapper


def _functioncomponent_builder(component_name, component_args, *args):
    if len(args) < 1:
        raise PrismValueError("need children (can be empty)")
    query = {
        "component_type": PrismComponentType.FUNCTION_COMPONENT,
        "component_name": component_name,
        "component_args": component_args,
        "children": [n._query for n in args],
        "nodeid": str(uuid.uuid4()),
    }
    if all([isinstance(c, _PrismFinancialComponent) for c in args if not isinstance(c, _PrismValue)]) & (
        component_name not in AggregateComponents
    ):
        return _PrismFinancialComponent(**query)
    return _PrismComponent(**query)


class _PrismComponent(_AbstractPrismComponent, ABC):
    """
    Args:
        query(dict): incl. component_type, component_name, component_args, children
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # simple operations
    @binary_operation
    def __add__(self, other):
        ...

    @binary_operation
    def __radd__(self, other):
        ...

    @binary_operation
    def __sub__(self, other):
        ...

    @binary_operation
    def __rsub__(self, other):
        ...

    @binary_operation
    def __mul__(self, other):
        ...

    @binary_operation
    def __rmul__(self, other):
        ...

    @binary_operation
    def __truediv__(self, other):
        ...

    @binary_operation
    def __rtruediv__(self, other):
        ...

    @binary_operation
    def __mod__(self, other):
        ...

    @binary_operation
    def __rmod__(self, other):
        ...

    @binary_operation
    def __pow__(self, other):
        ...

    @binary_operation
    def __rpow__(self, other):
        ...

    # logical operations
    @binary_operation
    def __eq__(self, other):
        ...

    @binary_operation
    def __ne__(self, other):
        ...

    @binary_operation
    def __gt__(self, other):
        ...

    @binary_operation
    def __ge__(self, other):
        ...

    @binary_operation
    def __lt__(self, other):
        ...

    @binary_operation
    def __le__(self, other):
        ...

    @binary_operation
    def __and__(self, other):
        ...

    @binary_operation
    def __or__(self, other):
        ...

    @binary_operation
    def __xor__(self, other):
        ...

    # other operations
    @operation
    def __invert__(self): ...

    @_validate_args
    def __getitem__(self, obj):
        if not isinstance(obj, _PrismComponent):
            raise PrismTypeError("mask should be a PrismComponent")

        if FUNCTIONS.get(obj._component_name)["type"] != "logical":
            raise PrismTypeError("mask should be a boolean components")

        if isinstance(obj, numbers.Real) or isinstance(obj, str):
            obj = SPECIALVALUEMAP.get(obj, obj)
            other_node = _PrismValue(data=obj)
        elif isinstance(obj, _PrismComponent):
            other_node = obj
        elif (self._component_name == "SecurityMaster") & isinstance(obj, str):
            obj = SPECIALVALUEMAP.get(obj, obj)
            other_node = _PrismValue(data=obj)
        else:
            raise PrismTypeError(f"unsupported operand type(s) for __getitem__: {type(self)}, {type(obj)}")

        return _functioncomponent_builder("__getitem__", {"obj": other_node._query}, self, other_node)

    @_validate_args
    @operation
    def resample(self, frequency: str, lookback: int, beyond: bool = True, drop_holiday: bool = False):
        """
        Resample time-series data. Up-samples or down-samples the input PrismComponent to the desired frequency and using the specified frequency and lookback.

        Parameters
        ----------

        frequency : str {'D', 'BD', 'W', 'BM', 'M', 'Q', 'A'}
            Desired sampling frequency to resample.

        lookback : int
            The periods to lookback are defined by the resampling frequency parameter. For example, if resampling to Monthly data, this will lookback *lookback* Months.

            .. admonition:: Note
                :class: note

                | When up-sampling, the lookback input parameter must be specified properly.
                |
                | For example, if resampling from Quarterly data to Monthly data, the lookback should be at least '3' or larger.
                | If set to only '1', then the lookback will not look far enough back to fill in every month and missing values will be left in the output time-series.
                | If no input is supplied, it will go back to the last data available and fill in every missing value in between.

        beyond : bool, default True
            Option to select whether to resample beyond the last data samples dates

        drop_holiday : bool, default False
            Option to select whether to drop holidays for each security during a resample

        Returns
        -------
            prism._PrismComponent
                Resampled timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close_daily = close.resample('D')
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> # upsampling
            >>> close_daily = close.resample('D')
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0          2586086  2010-01-04  47.57     AFL
            1          2586086  2010-01-05  48.95     AFL
            2          2586086  2010-01-06  49.38     AFL
            3          2586086  2010-01-07  49.91     AFL
            4          2586086  2010-01-08  49.41     AFL
            ...            ...         ...    ...     ...
            1095431  344286611  2011-10-27  44.31     ITT
            1095432  344286611  2011-10-28  44.99     ITT
            1095433  344286611  2011-10-29  44.99     ITT
            1095434  344286611  2011-10-30  44.99     ITT
            1095435  344286611  2011-10-31  45.60     ITT

            >>> # downsampling to monthly frequency
            >>> close_monthly = close.resample('M')
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                listingid        date  value  Ticker
            0        2586086  2010-01-31  48.43     AFL
            1        2586086  2010-02-28  49.45     AFL
            2        2586086  2010-03-31  54.29     AFL
            3        2586086  2010-04-30  50.96     AFL
            4        2586086  2010-05-31  44.30     AFL
            ...          ...         ...    ...     ...
            36045  344286611  2011-06-30  58.93     ITT
            36046  344286611  2011-07-31  53.34     ITT
            36047  344286611  2011-08-31  47.34     ITT
            36048  344286611  2011-09-30  42.00     ITT
            36049  344286611  2011-10-31  45.60     ITT
        """
        if (lookback is not None) and (lookback < 0):
            raise PrismValueError('lookback should be positive')

    @operation
    def round(self, decimals: int = 0):
        """
        Round each elements' value in a DataComponent to the given number of decimals.

        Parameters
        ----------
            decimals : int, default 0
                Number of decimal places to round to. If decimals is negative, it specifies the number of positions to the left of the decimal point.

        Returns
        -------
            prism._PrismComponent
                Rounded values of the Datacomponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.round() # 0 decimal point
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04   48.0     AFL
            1         2586086  2010-01-05   49.0     AFL
            2         2586086  2010-01-06   49.0     AFL
            3         2586086  2010-01-07   50.0     AFL
            4         2586086  2010-01-08   49.0     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25   44.0     ITT
            755972  344286611  2011-10-26   44.0     ITT
            755973  344286611  2011-10-27   44.0     ITT
            755974  344286611  2011-10-28   45.0     ITT
            755975  344286611  2011-10-31   46.0     ITT

            >>> close_result = close.round(1) # 1 decimal point
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04   47.6     AFL
            1         2586086  2010-01-05   49.0     AFL
            2         2586086  2010-01-06   49.4     AFL
            3         2586086  2010-01-07   49.9     AFL
            4         2586086  2010-01-08   49.4     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25   44.0     ITT
            755972  344286611  2011-10-26   43.5     ITT
            755973  344286611  2011-10-27   44.3     ITT
            755974  344286611  2011-10-28   45.0     ITT
            755975  344286611  2011-10-31   45.6     ITT
        """
        ...

    @operation
    def floor(self):
        """
        The floor value of each element. The floor of x i.e., the largest integer not greater than x.

        Returns
        -------
            prism._PrismComponent
                The floor of each element, with ``float`` dtype. This is a scalar if element is a scalar.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.floor()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04   47.0     AFL
            1         2586086  2010-01-05   48.0     AFL
            2         2586086  2010-01-06   49.0     AFL
            3         2586086  2010-01-07   49.0     AFL
            4         2586086  2010-01-08   49.0     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25   44.0     ITT
            755972  344286611  2011-10-26   43.0     ITT
            755973  344286611  2011-10-27   44.0     ITT
            755974  344286611  2011-10-28   44.0     ITT
            755975  344286611  2011-10-31   45.0     ITT
        """
        ...

    @operation
    def ceil(self):
        """
        The ceiling value of each element. The ceiling of x i.e., the smallest integer greater than or equal to x.

        Returns
        -------
            prism._PrismComponent
                The ceiling of each element, with ``float`` dtype. This is a scalar if element is a scalar.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.ceil()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04   48.0     AFL
            1         2586086  2010-01-05   49.0     AFL
            2         2586086  2010-01-06   50.0     AFL
            3         2586086  2010-01-07   50.0     AFL
            4         2586086  2010-01-08   50.0     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25   45.0     ITT
            755972  344286611  2011-10-26   44.0     ITT
            755973  344286611  2011-10-27   45.0     ITT
            755974  344286611  2011-10-28   45.0     ITT
            755975  344286611  2011-10-31   46.0     ITT

        """
        ...

    @operation
    def tanh(self):
        """
        Hyperbolic tangent value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | The corresponding hyperbolic tangent values.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.tanh()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04    1.0     AFL
            1         2586086  2010-01-05    1.0     AFL
            2         2586086  2010-01-06    1.0     AFL
            3         2586086  2010-01-07    1.0     AFL
            4         2586086  2010-01-08    1.0     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25    1.0     ITT
            755972  344286611  2011-10-26    1.0     ITT
            755973  344286611  2011-10-27    1.0     ITT
            755974  344286611  2011-10-28    1.0     ITT
            755975  344286611  2011-10-31    1.0     ITT
        """
        ...

    @operation
    def cosh(self):
        """
        Hyperbolic cosine value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | The corresponding hyperbolic cosine values.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.cosh()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date         value  Ticker
            0         2586086  2010-01-04  2.282225e+20     AFL
            1         2586086  2010-01-05  9.071621e+20     AFL
            2         2586086  2010-01-06  1.394542e+21     AFL
            3         2586086  2010-01-07  2.369232e+21     AFL
            4         2586086  2010-01-08  1.437012e+21     AFL
            ...           ...         ...           ...     ...
            755971  344286611  2011-10-25  6.555610e+18     ITT
            755972  344286611  2011-10-26  4.056502e+18     ITT
            755973  344286611  2011-10-27  8.761097e+18     ITT
            755974  344286611  2011-10-28  1.729333e+19     ITT
            755975  344286611  2011-10-31  3.182720e+19     ITT
        """
        ...

    @operation
    def sinh(self):
        """
        Hyperbolic sine value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | The corresponding hyperbolic sine values.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.sinh()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date         value  Ticker
            0         2586086  2010-01-04  2.282225e+20     AFL
            1         2586086  2010-01-05  9.071621e+20     AFL
            2         2586086  2010-01-06  1.394542e+21     AFL
            3         2586086  2010-01-07  2.369232e+21     AFL
            4         2586086  2010-01-08  1.437012e+21     AFL
            ...           ...         ...           ...     ...
            755971  344286611  2011-10-25  6.555610e+18     ITT
            755972  344286611  2011-10-26  4.056502e+18     ITT
            755973  344286611  2011-10-27  8.761097e+18     ITT
            755974  344286611  2011-10-28  1.729333e+19     ITT
            755975  344286611  2011-10-31  3.182720e+19     ITT
        """
        ...

    @operation
    def arcsinh(self):
        """
        Hyperbolic inverse sine value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | The hyperbolic inverse sine of each element in :math:`x`, in radians and in the closed interval \([-pi/2, pi/2])\. This is a scalar if :math:`x` is a scalar.
        """
        ...

    @operation
    def arccosh(self):
        """
        Return a DataComponet with hyperbolic inverse cosine value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                The hyperbolic inverse cosine of each element in PrismComponent, in radians and in the closed interval :math:`[-\pi/2, \pi/2]`.

        """
        ...

    @operation
    def arctanh(self):
        """
        Hyperbolic inverse tangent value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                The hyperbolic inverse tangent of each element in PrismComponent, in radians and in the closed interval :math:`[-\pi/2, \pi/2]`.
        """
        ...

    @operation
    def arctan(self):
        """
        Inverse tangent value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                The inverse tangent of each element in :math:`x`, in radians and in the closed interval :math:`[-\pi/2, \pi/2]`.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid       date  Close Ticker
            0         2586086 2010-01-04  47.57    AFL
            1         2586086 2010-01-05  48.95    AFL
            2         2586086 2010-01-06  49.38    AFL
            3         2586086 2010-01-07  49.91    AFL
            4         2586086 2010-01-08  49.41    AFL
            ...           ...        ...    ...    ...
            755971  344286611 2011-10-25  44.02    ITT
            755972  344286611 2011-10-26  43.54    ITT
            755973  344286611 2011-10-27  44.31    ITT
            755974  344286611 2011-10-28  44.99    ITT
            755975  344286611 2011-10-31  45.60    ITT

            >>> close_result = close.arctan()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value   Ticker
            0         2586086  2010-01-04  1.549778     AFL
            1         2586086  2010-01-05  1.550370     AFL
            2         2586086  2010-01-06  1.550548     AFL
            3         2586086  2010-01-07  1.550763     AFL
            4         2586086  2010-01-08  1.550560     AFL
            ...           ...         ...       ...     ...
            755975  344286611  2011-10-25  1.548083  ITT.WI
            755976  344286611  2011-10-26  1.547833  ITT.WI
            755977  344286611  2011-10-27  1.548232  ITT.WI
            755978  344286611  2011-10-28  1.548573  ITT.WI
            755979  344286611  2011-10-31  1.548870  ITT.WI
        """
        ...

    @operation
    def arccos(self):
        """
        Return a DataComponet with inverse cosine value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                The inverse cosine of each element in PrismComponent, in radians and in the closed interval :math:`[-\pi/2, \pi/2]`.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.arccos() # Input to arccos should be between 1 and 1. Values outside such range will yield NaNs
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04    NaN     AFL
            1         2586086  2010-01-05    NaN     AFL
            2         2586086  2010-01-06    NaN     AFL
            3         2586086  2010-01-07    NaN     AFL
            4         2586086  2010-01-08    NaN     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25    NaN     ITT
            755972  344286611  2011-10-26    NaN     ITT
            755973  344286611  2011-10-27    NaN     ITT
            755974  344286611  2011-10-28    NaN     ITT
            755975  344286611  2011-10-31    NaN     ITT

            >>> close_result = close.cross_sectional_percentile().arccos() # cross_sectional_percentile will yield values between 0 and 1, which makes suitable inputs to arccos
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  0.817564     AFL
            1         2586086  2010-01-05  0.778454     AFL
            2         2586086  2010-01-06  0.786962     AFL
            3         2586086  2010-01-07  0.778454     AFL
            4         2586086  2010-01-08  0.803766     AFL
            ...           ...         ...       ...     ...
            755971  344286611  2011-10-25  0.954521     ITT
            755972  344286611  2011-10-26  0.971575     ITT
            755973  344286611  2011-10-27  0.986035     ITT
            755974  344286611  2011-10-28  0.978823     ITT
            755975  344286611  2011-10-31  0.949610     ITT
        """
        ...

    @operation
    def arcsin(self):
        """
        Inverse sine value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | The inverse sine of each element in :math:`x`, in radians and in the closed interval :math:`[-\pi/2,\pi/2]`. This is a scalar if :math:`x` is a scalar.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid       date  Close Ticker
            0         2586086 2010-01-04  47.57    AFL
            1         2586086 2010-01-05  48.95    AFL
            2         2586086 2010-01-06  49.38    AFL
            3         2586086 2010-01-07  49.91    AFL
            4         2586086 2010-01-08  49.41    AFL
            ...           ...        ...    ...    ...
            755971  344286611 2011-10-25  44.02    ITT
            755972  344286611 2011-10-26  43.54    ITT
            755973  344286611 2011-10-27  44.31    ITT
            755974  344286611 2011-10-28  44.99    ITT
            755975  344286611 2011-10-31  45.60    ITT

            >>> close_result = close.arcsin() # Input to arcsin should be between 1 and 1. Values outside such range will yield NaNs.
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid       date  value Ticker
            0         2586086 2010-01-04    NaN    AFL
            1         2586086 2010-01-05    NaN    AFL
            2         2586086 2010-01-06    NaN    AFL
            3         2586086 2010-01-07    NaN    AFL
            4         2586086 2010-01-08    NaN    AFL
            ...           ...        ...    ...    ...
            755971  344286611 2011-10-25    NaN    ITT
            755972  344286611 2011-10-26    NaN    ITT
            755973  344286611 2011-10-27    NaN    ITT
            755974  344286611 2011-10-28    NaN    ITT
            755975  344286611 2011-10-31    NaN    ITT

            >>> close_result = close.cross_sectional_percentile().arcsin() # cross_sectional_percentile will yield values between 0 and 1, which makes suitable inputs to arcsin.
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  0.753232     AFL
            1         2586086  2010-01-05  0.792342     AFL
            2         2586086  2010-01-06  0.783834     AFL
            3         2586086  2010-01-07  0.792342     AFL
            4         2586086  2010-01-08  0.767030     AFL
            ...           ...         ...       ...     ...
            755971  344286611  2011-10-25  0.616276     ITT
            755972  344286611  2011-10-26  0.599222     ITT
            755973  344286611  2011-10-27  0.584761     ITT
            755974  344286611  2011-10-28  0.591974     ITT
            755975  344286611  2011-10-31  0.621186     ITT
        """
        ...

    @operation
    def tan(self):
        """
        Tangent value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | The corresponding tangent values.


        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.tan()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date       value  Ticker
            0         2586086  2010-01-04    0.478267     AFL
            1         2586086  2010-01-05   -3.831271     AFL
            2         2586086  2010-01-06   -1.223259     AFL
            3         2586086  2010-01-07   -0.371254     AFL
            4         2586086  2010-01-08   -1.150999     AFL
            ...           ...         ...         ...     ...
            755971  344286611  2011-10-25    0.037721     ITT
            755972  344286611  2011-10-26   -0.473590     ITT
            755973  344286611  2011-10-27    0.339960     ITT
            755974  344286611  2011-10-28    1.584115     ITT
            755975  344286611  2011-10-31  -21.303359     ITT
        """
        ...

    @operation
    def cos(self):
        """
        Cosine value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | The corresponding cosine values.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.cos()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  -0.902132     AFL
            1         2586086  2010-01-05   0.252549     AFL
            2         2586086  2010-01-06   0.632916     AFL
            3         2586086  2010-01-07   0.937479     AFL
            4         2586086  2010-01-08   0.655854     AFL
            ...           ...         ...        ...     ...
            755971  344286611  2011-10-25   0.999289     ITT
            755972  344286611  2011-10-26   0.903771     ITT
            755973  344286611  2011-10-27   0.946784     ITT
            755974  344286611  2011-10-28   0.533805     ITT
            755975  344286611  2011-10-31  -0.046889     ITT
        """
        ...

    @operation
    def sin(self):
        """
        Sine value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | The corresponding sine values.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.sin()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  -0.431460     AFL
            1         2586086  2010-01-05  -0.967584     AFL
            2         2586086  2010-01-06  -0.774220     AFL
            3         2586086  2010-01-07  -0.348043     AFL
            4         2586086  2010-01-08  -0.754887     AFL
            ...           ...         ...        ...     ...
            755971  344286611  2011-10-25   0.037694     ITT
            755972  344286611  2011-10-26  -0.428017     ITT
            755973  344286611  2011-10-27   0.321869     ITT
            755974  344286611  2011-10-28   0.845608     ITT
            755975  344286611  2011-10-31   0.998900     ITT
        """
        ...

    @operation
    def sqrt(self):
        """
        Square root value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | If any element in is complex, a complex array is returned (and the square-roots of negative reals are calculated).
                | If all of the elements are real, negative elements returning ``nan``.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.sqrt()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  6.897101     AFL
            1         2586086  2010-01-05  6.996428     AFL
            2         2586086  2010-01-06  7.027090     AFL
            3         2586086  2010-01-07  7.064701     AFL
            4         2586086  2010-01-08  7.029225     AFL
            ...           ...         ...       ...     ...
            755971  344286611  2011-10-25  6.634757     ITT
            755972  344286611  2011-10-26  6.598485     ITT
            755973  344286611  2011-10-27  6.656576     ITT
            755974  344286611  2011-10-28  6.707459     ITT
            755975  344286611  2011-10-31  6.752777     ITT
        """
        ...

    @_validate_args
    @operation
    def log_n(self, n: numbers.Real = 10):
        """
        Logarithm base n value of each element.

        Parameters
        ----------
            n : int, default 10
                Base of the logarithm

        Returns
        -------
            prism._PrismComponent
                The base-n logarithm of PrismComponent, element-wise.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> log_close = close.log_n()
            >>> log_close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  1.677333     AFL
            1         2586086  2010-01-05  1.689753     AFL
            2         2586086  2010-01-06  1.693551     AFL
            3         2586086  2010-01-07  1.698188     AFL
            4         2586086  2010-01-08  1.693815     AFL
            ...           ...         ...        ...     ...
            755971  344286611  2011-10-25  1.643650     ITT
            755972  344286611  2011-10-26  1.638888     ITT
            755973  344286611  2011-10-27  1.646502     ITT
            755974  344286611  2011-10-28  1.653116     ITT
            755975  344286611  2011-10-31  1.658965     ITT

        """
        ...

    @operation
    def ln(self):
        """
        The natural logarithm value of each element. The natural logarithm is logarithm in base :math:`e`.

        Returns
        -------
            prism._PrismComponent
                | The natural logarithm of PrismComponent, element-wise.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.ln()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  3.862202     AFL
            1         2586086  2010-01-05  3.890799     AFL
            2         2586086  2010-01-06  3.899545     AFL
            3         2586086  2010-01-07  3.910221     AFL
            4         2586086  2010-01-08  3.900153     AFL
            ...           ...         ...       ...     ...
            755971  344286611  2011-10-25  3.784644     ITT
            755972  344286611  2011-10-26  3.773680     ITT
            755973  344286611  2011-10-27  3.791210     ITT
            755974  344286611  2011-10-28  3.806440     ITT
            755975  344286611  2011-10-31  3.819908     ITT
        """
        ...

    @operation
    def exp(self):
        """
        Exponential value of each element.

        Returns
        -------
            prism._PrismComponent
                | Element-wise exponential of datacomponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.exp()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date         value  Ticker
            0         2586086  2010-01-04  4.564451e+20     AFL
            1         2586086  2010-01-05  1.814324e+21     AFL
            2         2586086  2010-01-06  2.789083e+21     AFL
            3         2586086  2010-01-07  4.738464e+21     AFL
            4         2586086  2010-01-08  2.874024e+21     AFL
            ...           ...         ...           ...     ...
            755971  344286611  2011-10-25  1.311122e+19     ITT
            755972  344286611  2011-10-26  8.113005e+18     ITT
            755973  344286611  2011-10-27  1.752219e+19     ITT
            755974  344286611  2011-10-28  3.458667e+19     ITT
            755975  344286611  2011-10-31  6.365439e+19     ITT
        """
        ...

    @operation
    def __abs__(self):
        """
        Absolute value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | Absolute values of the Datacomponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close_result = close.sin()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  -0.431460     AFL
            1         2586086  2010-01-05  -0.967584     AFL
            2         2586086  2010-01-06  -0.774220     AFL
            3         2586086  2010-01-07  -0.348043     AFL
            4         2586086  2010-01-08  -0.754887     AFL
            ...           ...         ...        ...     ...
            755971  344286611  2011-10-25   0.037694     ITT
            755972  344286611  2011-10-26  -0.428017     ITT
            755973  344286611  2011-10-27   0.321869     ITT
            755974  344286611  2011-10-28   0.845608     ITT
            755975  344286611  2011-10-31   0.998900     ITT

            >>> abs_result = abs(close_result)
            >>> abs_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  0.431460     AFL
            1         2586086  2010-01-05  0.967584     AFL
            2         2586086  2010-01-06  0.774220     AFL
            3         2586086  2010-01-07  0.348043     AFL
            4         2586086  2010-01-08  0.754887     AFL
            ...           ...         ...       ...     ...
            755971  344286611  2011-10-25  0.037694     ITT
            755972  344286611  2011-10-26  0.428017     ITT
            755973  344286611  2011-10-27  0.321869     ITT
            755974  344286611  2011-10-28  0.845608     ITT
            755975  344286611  2011-10-31  0.998900     ITT
        """
        ...

    @operation
    def abs(self):
        """
        Absolute value of each element.
        This function only applies to elements that are all numeric.

        Returns
        -------
            prism._PrismComponent
                | Absolute values of the Datacomponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close_result = close.sin()
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  -0.431460     AFL
            1         2586086  2010-01-05  -0.967584     AFL
            2         2586086  2010-01-06  -0.774220     AFL
            3         2586086  2010-01-07  -0.348043     AFL
            4         2586086  2010-01-08  -0.754887     AFL
            ...           ...         ...        ...     ...
            755971  344286611  2011-10-25   0.037694     ITT
            755972  344286611  2011-10-26  -0.428017     ITT
            755973  344286611  2011-10-27   0.321869     ITT
            755974  344286611  2011-10-28   0.845608     ITT
            755975  344286611  2011-10-31   0.998900     ITT

            >>> abs_result = abs(close_result)
            >>> abs_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  0.431460     AFL
            1         2586086  2010-01-05  0.967584     AFL
            2         2586086  2010-01-06  0.774220     AFL
            3         2586086  2010-01-07  0.348043     AFL
            4         2586086  2010-01-08  0.754887     AFL
            ...           ...         ...       ...     ...
            755971  344286611  2011-10-25  0.037694     ITT
            755972  344286611  2011-10-26  0.428017     ITT
            755973  344286611  2011-10-27  0.321869     ITT
            755974  344286611  2011-10-28  0.845608     ITT
            755975  344286611  2011-10-31  0.998900     ITT
        """
        ...

    @_validate_args
    @operation
    def isin(self, values: list):
        """
        Whether each element in the Data Component is contained in values.

        Parameters
        ----------
            values : list

        Returns
        -------
            prism._PrismComponent
                DataComponent of booleans showing whether each element is contained in values.
        """
        ...

    @_validate_args
    def fillna(self, value: Union[str, float, int, _AbstractPrismComponent] = None, method: str = None, n: int = None):
        """
        Fill NA/NaN values using the specified method.

        Parameters
        ----------
            value : PrismComponent, str, int, float, default None
                Value to use to fill NaN values (e.g. 0), alternately for a PrismComponent input, it will fill values based on matching columns (i.e id, date etc)

            method : str {'backfill', 'bfill', 'pad', 'ffill', None}, default None
                | Method to use for filling NaN in

                - pad / ffill: Propagate last valid observation forward to next valid
                - backfilfillnal / bfill: Use next valid observation to fill gap

            n : int, default None
                | If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill.
                | If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled.
                | Must be greater than 0 if not None.

                .. admonition:: Warning
                    :class: warning

                    If the number of consecutive NaNs are greater than n , it will only be partially filled.

        Returns
        -------
            prism._PrismComponent

        Examples
        --------
            >>> rd = prism.financial.income_statement(dataitemid=100602, periodtype='Q')
            >>> rd_df = rd.get_data(universe=1, startdate='2019-01-31', enddate='2022-08-31')
            >>> rd_df
                    listingid        date  currency      period  R&D Expense
            0         20106319  2019-02-20       THB  2018-12-31          NaN
            1         20106319  2019-04-24       THB  2019-03-31          NaN
            2         20106319  2019-08-08       THB  2019-06-30          NaN
            3         20106319  2019-11-06       THB  2019-09-30          NaN
            4         20106319  2020-02-26       THB  2019-12-31          NaN
            ...            ...         ...       ...         ...          ...
            103101  1780525435  2022-08-12       INR  2022-06-30          NaN
            103103  1780926579  2022-08-23       AUD  2022-06-30          NaN
            103106  1781170875  2022-08-12       INR  2022-06-30          NaN
            103111  1781747464  2022-08-08       INR  2022-06-30          NaN
            103120  1784786390  2022-08-19       MYR  2022-06-30          NaN

            >>> rd_no_na = rd.fillna(0)
            >>> rd_no_na_df = rd_no_na .get_data(universe=1, startdate='2019-01-31', enddate='2022-08-31')
            >>> rd_no_na_df
                    listingid        date  currency      period  R&D Expense
            0         20106319  2019-02-20       THB  2018-12-31          0.0
            1         20106319  2019-04-24       THB  2019-03-31          0.0
            2         20106319  2019-08-08       THB  2019-06-30          0.0
            3         20106319  2019-11-06       THB  2019-09-30          0.0
            4         20106319  2020-02-26       THB  2019-12-31          0.0
            ...            ...         ...       ...         ...          ...
            103101  1780525435  2022-08-12       INR  2022-06-30          0.0
            103103  1780926579  2022-08-23       AUD  2022-06-30          0.0
            103106  1781170875  2022-08-12       INR  2022-06-30          0.0
            103111  1781747464  2022-08-08       INR  2022-06-30          0.0
            103120  1784786390  2022-08-19       MYR  2022-06-30          0.0
        """
        other_node = None
        if value is not None:
            if isinstance(value, numbers.Real) or isinstance(value, str):
                value = SPECIALVALUEMAP.get(value, value)
                other_node = _PrismValue(data=value)
            elif isinstance(value, _PrismComponent):
                other_node = value
            else:
                raise PrismTypeError(f"unsupported operand type(s) for fillna: {type(self)}, {type(value)}")
        component_args = {'method': method, 'n': n}
        args = [self]
        if other_node:
            args.append(other_node)
        return _functioncomponent_builder('fillna', component_args, *args)

    # n-period operations
    @_validate_args
    @n_period_operation
    @operation
    def n_periods_pct_change(self, n: int, positive_denominator: bool = False):
        """
        Percentage change between the current and a prior ``n``th element. Computes the percentage change from the immediately previous row by default if no ``n`` is given. This is useful in comparing the percentage of change in a time series of elements.

        Parameters
        ----------
            n : int
                Periods to shift for calculating percent change, accepts negative values.

            positive_denominator : bool, default False
                Whether to only include result of positive denominator. The result from negative or zero denominator will be assigned ``np.nan`` .

        Returns
        -------
            prism._PrismComponent
                Percent change of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_pct_change(n=1)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  0.028541     AFL
            1         2586086  2010-01-05  0.029010     AFL
            2         2586086  2010-01-06  0.008784     AFL
            3         2586086  2010-01-07  0.010733     AFL
            4         2586086  2010-01-08 -0.010018     AFL
            ...           ...         ...       ...     ...
            755903  344286611  2011-10-25 -0.013226     ITT
            755904  344286611  2011-10-26 -0.010904     ITT
            755905  344286611  2011-10-27  0.017685     ITT
            755906  344286611  2011-10-28  0.015346     ITT
            755907  344286611  2011-10-31  0.013559     ITT
        """
        ...

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_shift(self, n: int):
        """
        Shift all PrismComponent element by n periods.

        Parameters
        ----------
            n : int
                Number of periods to shift. Can be positive or negative.

        Returns
        -------
            prism._PrismComponent
                Shifted values of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_shift(n=2)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04  46.88     AFL
            1         2586086  2010-01-05  46.25     AFL
            2         2586086  2010-01-06  47.57     AFL
            3         2586086  2010-01-07  48.95     AFL
            4         2586086  2010-01-08  49.38     AFL
            ...           ...         ...    ...     ...
            755859  344286611  2011-10-25  44.25     ITT
            755860  344286611  2011-10-26  44.61     ITT
            755861  344286611  2011-10-27  44.02     ITT
            755862  344286611  2011-10-28  43.54     ITT
            755863  344286611  2011-10-31  44.31     ITT
        """
        ...

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_diff(self, n: int):
        """
        Difference between the current and a prior ``n``th element. Computes the difference from the immediately previous row by default if no ``n`` is given.


        Parameters
        ----------
            n : int
                Periods to shift for calculating difference, accepts negative values.

        Returns
        -------
            prism._PrismComponent
                First differences of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> log_close = close.n_periods_diff(5)
            >>> log_close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date   value  Ticker
            0         2586086  2010-01-04   0.78      AFL
            1         2586086  2010-01-05   2.15      AFL
            2         2586086  2010-01-06   2.43      AFL
            3         2586086  2010-01-07   3.03      AFL
            4         2586086  2010-01-08   3.16      AFL
            ...           ...         ...    ...      ...
            755971  344286611  2011-10-25  -0.94      ITT
            755972  344286611  2011-10-26  -0.61      ITT
            755973  344286611  2011-10-27   0.61      ITT
            755974  344286611  2011-10-28   0.74      ITT
            755975  344286611  2011-10-31   0.99      ITT
        """
        ...

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_max(self, n: int, min_periods: int = 1, weights: list = None):
        """
        Maximum of the values over given period n.

        Parameters
        ----------
            n : int
                Periods for calculating maximum values, accepts negative values.

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period maximum timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> n_max= close.n_periods_max(n=2)
            >>> n_max.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.91     AFL
            ...           ...         ...    ...     ...
            755947  344286611  2011-10-25  44.61     ITT
            755948  344286611  2011-10-26  44.02     ITT
            755949  344286611  2011-10-27  44.31     ITT
            755950  344286611  2011-10-28  44.99     ITT
            755951  344286611  2011-10-31  45.60     ITT
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_min(self, n: int, min_periods: int = 1, weights: list = None):
        """
        Minimum of the values over given period n.

        Parameters
        ----------
            n : int
                Periods for calculating minimum values, accepts negative values.

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period minimum timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_min(n=2)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04  46.25     AFL
            1         2586086  2010-01-05  47.57     AFL
            2         2586086  2010-01-06  48.95     AFL
            3         2586086  2010-01-07  49.38     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755947  344286611  2011-10-25  44.02     ITT
            755948  344286611  2011-10-26  43.54     ITT
            755949  344286611  2011-10-27  43.54     ITT
            755950  344286611  2011-10-28  44.31     ITT
            755951  344286611  2011-10-31  44.99     ITT
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_mean(self, n: int, min_periods: int = 1, weights: list = None):
        r"""
        Mean of the values over given period n.

        Parameters
        ----------
            n : int
                | Periods for calculating mean values, accepts negative values.

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period mean timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_mean(n=5)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date   value  Ticker
            0         2586086  2010-01-04  46.890     AFL
            1         2586086  2010-01-05  47.320     AFL
            2         2586086  2010-01-06  47.806     AFL
            3         2586086  2010-01-07  48.412     AFL
            4         2586086  2010-01-08  49.044     AFL
            ...           ...         ...     ...     ...
            755887  344286611  2011-10-25  44.146     ITT
            755888  344286611  2011-10-26  44.024     ITT
            755889  344286611  2011-10-27  44.146     ITT
            755890  344286611  2011-10-28  44.294     ITT
            755891  344286611  2011-10-31  44.492     ITT
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")


    @_validate_args
    @n_period_operation
    @operation
    def n_periods_ewma(self, n: int, min_periods: int = 1):
        r"""
        Exponential moving average over given period n.

        .. math:: EWMA_t = ar_t - (1-a)EWMA_(t-1)

        Parameters
        ----------
            n : int
                | Span for calculating exponential moving average, accepts negative values.

                .. math:: a = \frac{2}{n+1}

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

        Returns
        -------
            prism._PrismComponent
                Exponential moving standard deviation of the PrismComponent.

        """
        ...


    @_validate_args
    @n_period_operation
    @operation
    def n_periods_ewmstd(self, n: int, min_periods: int = 1):
        r"""
        Exponential moving standard deviation over given period n.

        .. math:: EWMA_t = ar_t - (1-a)EWMA_(t-1)

        Parameters
        ----------
            n : int
                | Span for calculating exponential moving average, accepts negative values.

                .. math:: a = \frac{2}{n+1}

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

        Returns
        -------
            prism._PrismComponent
                Exponential moving average of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_ewma(n=5)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  46.976135     AFL
            1         2586086  2010-01-05  47.674993     AFL
            2         2586086  2010-01-06  48.266404     AFL
            3         2586086  2010-01-07  48.828901     AFL
            4         2586086  2010-01-08  49.026019     AFL
            ...           ...         ...        ...     ...
            755887  344286611  2011-10-25  44.262644     ITT
            755888  344286611  2011-10-26  44.021763     ITT
            755889  344286611  2011-10-27  44.117842     ITT
            755890  344286611  2011-10-28  44.408561     ITT
            755891  344286611  2011-10-31  44.805707     ITT
        """
        ...

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_ewmvar(self, n: int, min_periods: int = 1):
        r"""
        Exponential moving standard variance over given period n.

        .. math:: EWMA_t = ar_t - (1-a)EWMA_(t-1)

        Parameters
        ----------
            n : int
                | Span for calculating exponential moving average, accepts negative values.

                | .. math:: a = \frac{2}{n+1}

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period variance timeseries of the PrismComponent.

        """
        ...

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_median(self, n: int, min_periods: int = 1, weights: list = None):
        r"""
        Median of the values over given period n.

        Parameters
        ----------
            n : int
                | Periods for calculating median values, accepts negative values.

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period median timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_median(n=3)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04  46.88     AFL
            1         2586086  2010-01-05  47.57     AFL
            2         2586086  2010-01-06  48.95     AFL
            3         2586086  2010-01-07  49.38     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755919  344286611  2011-10-25  44.25     ITT
            755920  344286611  2011-10-26  44.02     ITT
            755921  344286611  2011-10-27  44.02     ITT
            755922  344286611  2011-10-28  44.31     ITT
            755923  344286611  2011-10-31  44.99     ITT
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_sum(self, n: int, min_periods: int = 1, weights: list = None):
        r"""
        The sum of the values over given period n.

        Parameters
        ----------
            n : int
                | Periods for calculating sum values, accepts negative values.

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period sum timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_sum(n=2)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04  93.82     AFL
            1         2586086  2010-01-05  96.52     AFL
            2         2586086  2010-01-06  98.33     AFL
            3         2586086  2010-01-07  99.29     AFL
            4         2586086  2010-01-08  99.32     AFL
            ...           ...         ...    ...     ...
            755947  344286611  2011-10-25  88.63     ITT
            755948  344286611  2011-10-26  87.56     ITT
            755949  344286611  2011-10-27  87.85     ITT
            755950  344286611  2011-10-28  89.30     ITT
            755951  344286611  2011-10-31  90.59     ITT
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_std(self, n: int, min_periods: int = 1, weights: list = None):
        r"""
        Standard deviation of the values over given period n.

        Parameters
        ----------
            n : int
                | Periods for calculating standard deviation values, accepts negative values.

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period standard deviation timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_std(n=5)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  0.470053     AFL
            1         2586086  2010-01-05  1.024061     AFL
            2         2586086  2010-01-06  1.334215     AFL
            3         2586086  2010-01-07  1.487757     AFL
            4         2586086  2010-01-08  0.891392     AFL
            ...           ...         ...       ...     ...
            755887  344286611  2011-10-25  0.332009     ITT
            755888  344286611  2011-10-26  0.428287     ITT
            755889  344286611  2011-10-27  0.398786     ITT
            755890  344286611  2011-10-28  0.554103     ITT
            755891  344286611  2011-10-31  0.812078     ITT
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_var(self, n: int, min_periods: int = 1, weights: list = None):
        r"""
        Variance of the values over given period n.

        Parameters
        ----------
            n : int
                | Periods for calculating variance values, accepts negative values.

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period variance timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_var(n=5)
            TODO
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_z_score(self, n: int, min_periods: int = 1, weights: list = None):
        r"""
        Z-score of the values over given period n.

        Parameters
        ----------
            n : int
                | Periods for calculating z-score values, accepts negative values.

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period z-score timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_z_score(n=5)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date      value  Ticker
            0         2586086  2010-01-04   1.446645     AFL
            1         2586086  2010-01-05   1.591703     AFL
            2         2586086  2010-01-06   1.179720     AFL
            3         2586086  2010-01-07   1.006885     AFL
            4         2586086  2010-01-08   0.410594     AFL
            ...           ...         ...        ...     ...
            755885  344286611  2011-10-25  -0.379508     ITT
            755886  344286611  2011-10-26  -1.130083     ITT
            755887  344286611  2011-10-27   0.411248     ITT
            755888  344286611  2011-10-28   1.256084     ITT
            755889  344286611  2011-10-31   1.364402     ITT
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_skew(self, n: int, min_periods: int = 1, weights: list = None):
        r"""
        Skewness of the values over given period n.

        Parameters
        ----------
            n : int
                | Periods for calculating skewness values, accepts negative values.

            min_periods : int, default 1
                Minimum number of observations in window required to have a value; otherwise, result is ``np.nan`` .

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n period skewness timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_skew(n=5)
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  0.207711     AFL
            1         2586086  2010-01-05  1.158318     AFL
            2         2586086  2010-01-06  0.144256     AFL
            3         2586086  2010-01-07 -0.794403     AFL
            4         2586086  2010-01-08 -1.451241     AFL
            ...           ...         ...       ...     ...
            755885  344286611  2011-10-25  0.117328     ITT
            755886  344286611  2011-10-26  0.346765     ITT
            755887  344286611  2011-10-27 -0.782576     ITT
            755888  344286611  2011-10-28 -0.197206     ITT
            755889  344286611  2011-10-31  0.396619     ITT
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_periods_kurt(self, n: int, min_periods: int = 1):
        """
        TODO
        """
        ...

    # cross-sectional operations
    @_validate_args
    @cross_sectional_operation
    def cross_sectional_rank(self, rank_method: str = "standard", ascending: bool = True):
        """
        Numerical data ranks (1 through n) across each date for each element.

        Parameters
        ----------
            rank_method : str {'standard', 'modified', 'dense', 'ordinal', 'fractional'}, default 'standard'
                | Method for how equal values are assigned a rank.

                - standard: 1 2 2 4
                - modified: 1 3 3 4
                - dense: 1 2 2 3
                - ordinal: 1 2 3 4
                - fractional: 1 2.5 2.5 4

            ascending : bool, default True
                Whether or not the elements should be ranked in ascending order.

        Returns
        -------
            prism._PrismComponent
                Cross sectional ranking of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_pct_change(21).cross_sectional_rank() # trading month momentum cross sectional ranking
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04  187.0     AFL
            1         2586086  2010-01-05  337.0     AFL
            2         2586086  2010-01-06  355.0     AFL
            3         2586086  2010-01-07  368.0     AFL
            4         2586086  2010-01-08  314.0     AFL
            ...           ...         ...    ...     ...
            755337  344286611  2011-10-25  150.0     ITT
            755338  344286611  2011-10-26   78.0     ITT
            755339  344286611  2011-10-27   63.0     ITT
            755340  344286611  2011-10-28   76.0     ITT
            755341  344286611  2011-10-31  166.0     ITT
        """
        ...

    @_validate_args
    @cross_sectional_operation
    def cross_sectional_percentile(self, rank_method: str = "standard", ascending: bool = True):
        """
        Numerical data percentiles (between 0 and 1) across each date for each element.

        Parameters
        ----------
            rank_method : str {'standard', 'modified', 'dense', 'ordinal', 'fractional'}, default 'standard'
                | Method for how equal values are assigned a rank.

                - standard: 1 2 2 4
                - modified: 1 3 3 4
                - dense: 1 2 2 3
                - ordinal: 1 2 3 4
                - fractional: 1 2.5 2.5 4

            ascending : bool, default True
                Whether or not the elements should be ranked in ascending order.

        Returns
        -------
            prism._PrismComponent
                Group percentile timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> cross_percentile = close.cross_sectional_percentile()
            >>> cross_percentile.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04  0.684    AFL
            1         2586086  2010-01-05  0.712    AFL
            2         2586086  2010-01-06  0.706    AFL
            3         2586086  2010-01-07  0.712    AFL
            4         2586086  2010-01-08  0.694    AFL
            ...           ...         ...    ...    ...
            755971  344286611  2011-10-25  0.578    ITT
            755972  344286611  2011-10-26  0.564    ITT
            755973  344286611  2011-10-27  0.552    ITT
            755974  344286611  2011-10-28  0.558    ITT
            755975  344286611  2011-10-31  0.582    ITT
        """
        ...

    @_validate_args
    @cross_sectional_operation
    def cross_sectional_quantile(
        self,
        bins: int,
        rank_method: str = "standard",
        ascending: bool = True,
        right: bool = True,
    ):
        """
        Numerical quantiles across each date for each element.

        Parameters
        ----------
            bins : int
                Number of quantiles. 10 for deciles, 4 for quartiles, etc.

            rank_method : str {'standard', 'modified', 'dense', 'ordinal', 'fractional'}, default 'standard'
                | Method for how equal values are assigned a rank.

                - standard: 1 2 2 4
                - modified: 1 3 3 4
                - dense: 1 2 2 3
                - ordinal: 1 2 3 4
                - fractional: 1 2.5 2.5 4

            ascending : bool, default True
                Whether or not the elements should be ranked in ascending order.

            right : bool, default True
                | If True, given a border value in between bins, whether to put the sample in the which bins.
                | For example, if the value borders for bin 1 is between 0 ~ 5 and bin 2 is between 5 ~ 10, if right is True, and a sample has a value 5, then it will be assigned bin 1. if False, then bin 2.

        Returns
        -------
            prism._PrismComponent
                Group percentile timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_pct_change(21).cross_sectional_quantile(5) #trading month momentum cross sectional quantile
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04    2.0     AFL
            1         2586086  2010-01-05    4.0     AFL
            2         2586086  2010-01-06    4.0     AFL
            3         2586086  2010-01-07    4.0     AFL
            4         2586086  2010-01-08    4.0     AFL
            ...           ...         ...    ...     ...
            755337  344286611  2011-10-25    2.0     ITT
            755338  344286611  2011-10-26    1.0     ITT
            755339  344286611  2011-10-27    1.0     ITT
            755340  344286611  2011-10-28    1.0     ITT
            755341  344286611  2011-10-31    2.0     ITT
        """
        ...

    @cross_sectional_operation
    def cross_sectional_z_score(self):
        """
        Z-score of the values over across each date for each element.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group z-score timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # data component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_z_score(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])\
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  -0.015607     AFL
            1         2586086  2010-01-05   0.421663     AFL
            2         2586086  2010-01-06   0.754689     AFL
            3         2586086  2010-01-07   0.282194     AFL
            4         2586086  2010-01-08   0.051700     AFL
            ...           ...         ...        ...     ...
            755337  344286611  2011-10-25  -0.891504     ITT
            755338  344286611  2011-10-26  -1.087371     ITT
            755339  344286611  2011-10-27  -1.296089     ITT
            755340  344286611  2011-10-28  -1.136280     ITT
            755341  344286611  2011-10-31  -0.707442     ITT
        """
        ...

    @cross_sectional_operation
    def cross_sectional_demean(self):
        """
        Demean of the values over across each date for each element.


        Returns
        -------
            prism._PrismComponent
                Cross sectional demean timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_pct_change(21).cross_sectional_demean() #trading month momentum cross sectional z-score
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  -0.025406     AFL
            1         2586086  2010-01-05   0.017973     AFL
            2         2586086  2010-01-06   0.024147     AFL
            3         2586086  2010-01-07   0.031885     AFL
            4         2586086  2010-01-08   0.005299     AFL
            ...           ...         ...        ...     ...
            755337  344286611  2011-10-25  -0.035976     ITT
            755338  344286611  2011-10-26  -0.063636     ITT
            755339  344286611  2011-10-27  -0.105008     ITT
            755340  344286611  2011-10-28  -0.094468     ITT
            755341  344286611  2011-10-31  -0.046099     ITT
        """
        ...

    @cross_sectional_operation
    def cross_sectional_sum(self):
        """
        Sum of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional sum timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> cross_sum = close.cross_sectional_sum()
            >>> cross_sum.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                        date	     value
            0	    2010-01-04	21878.8753
            1	    2010-01-05	21932.3200
            2	    2010-01-06	21980.7800
            3	    2010-01-07	22052.8920
            4	    2010-01-08	22144.2920
            ...	         ...	       ...
            1505  2015-12-24	41419.2350
            1506  2015-12-28	41388.1900
            1507  2015-12-29	41858.7300
            1508  2015-12-30	41575.1400
            1509  2015-12-31	41211.8500
        """
        ...

    @cross_sectional_operation
    def cross_sectional_max(self):
        """
        Maximum of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional max timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> cross_max = close.cross_sectional_max()
            >>> cross_max.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                        date	  value
            0	    2010-01-04	 626.75
            1	    2010-01-05	 623.99
            2	    2010-01-06	 608.26
            3	    2010-01-07	 594.10
            4	    2010-01-08	 602.02
            ...	         ...	    ...
            1505  2015-12-24	1273.07
            1506  2015-12-28	1272.96
            1507  2015-12-29	1302.40
            1508  2015-12-30	1289.16
            1509  2015-12-31	1274.95
        """
        ...

    @cross_sectional_operation
    def cross_sectional_min(self):
        """
        Minimum of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional min timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> cross_min = close.cross_sectional_min()
            >>> cross_min.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                        date  value
            0	    2010-01-04   1.84
            1	    2010-01-05   1.80
            2	    2010-01-06   1.79
            3	    2010-01-07   1.80
            4	    2010-01-08   1.80
            ...	         ...	  ...
            1505  2015-12-24   4.45
            1506  2015-12-28   4.07
            1507  2015-12-29   4.58
            1508  2015-12-30   4.40
            1509  2015-12-31   4.50
        """
        ...

    @cross_sectional_operation
    def cross_sectional_mean(self):
        """
        Mean of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional mean timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> cross_mean = close..cross_sectional_mean()
            >>> cross_mean.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                        date     value
            0       2010-01-04  1.677333
            1       2010-01-05  1.689753
            2       2010-01-06  1.693551
            3       2010-01-07  1.698188
            4       2010-01-08  1.693815
            ...            ...       ...
            755971  2011-10-25  1.643650
            755972  2011-10-26  1.638888
            755973  2011-10-27  1.646502
            755974  2011-10-28  1.653116
            755975  2011-10-31  1.658965
        """
        ...

    @cross_sectional_operation
    def cross_sectional_std(self):
        """
        Standard deviation of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional standard deviation timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> close_result = close.n_periods_pct_change(21).cross_sectional_std() #trading month momentum cross sectional z-score
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  -0.025406     AFL
            1         2586086  2010-01-05   0.017973     AFL
            2         2586086  2010-01-06   0.024147     AFL
            3         2586086  2010-01-07   0.031885     AFL
            4         2586086  2010-01-08   0.005299     AFL
            ...           ...         ...        ...     ...
            755337  344286611  2011-10-25  -0.035976     ITT
            755338  344286611  2011-10-26  -0.063636     ITT
            755339  344286611  2011-10-27  -0.105008     ITT
            755340  344286611  2011-10-28  -0.094468     ITT
            755341  344286611  2011-10-31  -0.046099     ITT
        """
        ...

    @cross_sectional_operation
    def cross_sectional_median(self):
        """
        Median of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional median timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> cross_median = close.cross_sectional_median()
            >>> cross_median.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                        date   value
            0       2010-01-04  35.575
            1       2010-01-05  35.390
            2       2010-01-06  35.365
            3       2010-01-07  35.230
            4       2010-01-08  35.300
            ...            ...     ...
            755971  2011-10-25  60.525
            755972  2011-10-26  60.410
            755973  2011-10-27  61.270
            755974  2011-10-28  60.905
            755975  2011-10-31  60.040
        """
        ...

    @cross_sectional_operation
    def cross_sectional_count(self):
        """
        Count of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional count timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            >>> cross_count = close.cross_sectional_count()
            >>> cross_count.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                        date	value
            0	    2010-01-04	  500
            1	    2010-01-05	  500
            2	    2010-01-06	  500
            3	    2010-01-07	  500
            4	    2010-01-08	  500
            ...	         ...	  ...
            1505  2015-12-24	  504
            1506  2015-12-28	  504
            1507  2015-12-29	  504
            1508  2015-12-30	  504
            1509  2015-12-31	  504
        """
        ...

    @cross_sectional_operation
    def cross_sectional_skew(self):
        """
        Skewness of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional skewness timeseries of the PrismComponent.

        Examples
        --------
        TODO
        """
        ...

    @cross_sectional_operation
    def cross_sectional_kurt(self):
        """
        Kurtosis of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional kurtosis timeseries of the PrismComponent.

        Examples
        --------
        TODO
        """
        ...

    @cross_sectional_operation
    def cross_sectional_mode(self):
        """
        Mode of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional mode timeseries of the PrismComponent.

        Examples
        --------
        TODO
        """
        ...

    @cross_sectional_operation
    def cross_sectional_prod(self):
        """
        Product of the values over across each date.

        Returns
        -------
            prism._PrismComponent
                Cross sectional product timeseries of the PrismComponent.

        Examples
        --------
        TODO
        """
        ...

    # group operations
    @group_operation
    def group_mean(self, group):
        """
        Mean of values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group mean timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # Data Component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_mean(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                   GICS sector        date	   value
            0	          10.0  2010-01-04	0.082004
            1	          10.0	2010-01-05	0.118139
            2	          10.0  2010-01-06	0.142810
            3	          10.0  2010-01-07	0.142869
            4	          10.0  2010-01-08	0.181065
            ...	           ...         ...	     ...
            15095         55.0  2015-12-24	0.014816
            15096         55.0  2015-12-28	0.023774
            15097         55.0  2015-12-29	0.028174
            15098         55.0  2015-12-30	0.021684
            15099         55.0  2015-12-31	0.005876
        """
        ...

    @group_operation
    def group_std(self, group):
        """
        Standard deviation of values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group standard deviation timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # data component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_std(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                   GICS sector        date	   value
            0	          10.0  2010-01-04	0.070820
            1	          10.0  2010-01-05	0.078481
            2	          10.0  2010-01-06	0.080737
            3	          10.0  2010-01-07	0.081728
            4	          10.0  2010-01-08	0.091463
            ...	           ...         ...	     ...
            15095         55.0  2015-12-24	0.032398
            15096         55.0  2015-12-28	0.031411
            15097         55.0  2015-12-29	0.027771
            15098         55.0  2015-12-30	0.036954
            15099         55.0  2015-12-31	0.028405
        """
        ...

    @group_operation
    def group_min(self, group):
        """
        Minimum of values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group min timeseries of the PrismComponent

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # Data Component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_min(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                   GICS sector        date	    value
            0	          10.0  2010-01-04	-0.087611
            1	          10.0	2010-01-05	-0.074277
            2	          10.0  2010-01-06	-0.056970
            3	          10.0  2010-01-07	-0.053816
            4	          10.0  2010-01-08	-0.047019
            ...	           ...         ...	      ...
            15095         55.0  2015-12-24	-0.088748
            15096         55.0  2015-12-28	-0.066502
            15097         55.0  2015-12-29	-0.038038
            15098         55.0  2015-12-30	-0.102751
            15099         55.0  2015-12-31	-0.060464
        """
        ...

    @group_operation
    def group_max(self, group):
        """
        Maximum of values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group max timeseries of the PrismComponent

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # Data Component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_max(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                   GICS sector        date	   value
            0	          10.0  2010-01-04	0.205486
            1	          10.0	2010-01-05	0.257924
            2	          10.0  2010-01-06	0.326705
            3	          10.0  2010-01-07	0.329350
            4	          10.0  2010-01-08	0.390691
            ...	           ...         ...	     ...
            15095         55.0  2015-12-24	0.061547
            15096         55.0  2015-12-28	0.064403
            15097         55.0  2015-12-29	0.085882
            15098         55.0  2015-12-30	0.079646
            15099         55.0  2015-12-31	0.080636
        """
        ...

    @group_operation
    def group_sum(self, group):
        """
        Sum of values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group sum timeseries of the PrismComponent

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # Data Component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_sum(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                   GICS sector        date	   value
            0	          10.0  2010-01-04	3.198166
            1	          10.0	2010-01-05	4.607422
            2	          10.0  2010-01-06	5.569585
            3	          10.0  2010-01-07	5.571885
            4	          10.0  2010-01-08	7.061548
            ...	           ...         ...	     ...
            15095         55.0  2015-12-24	0.429676
            15096         55.0  2015-12-28	0.689446
            15097         55.0  2015-12-29	0.817036
            15098         55.0  2015-12-30	0.628850
            15099         55.0  2015-12-31	0.170396
        """
        ...

    @group_operation
    def group_count(self, group):
        """
        Count of values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group count timeseries of the PrismComponent

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # Data Component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_count(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                   GICS sector        date	value
            0	          10.0  2010-01-04	   39
            1	          10.0  2010-01-05	   39
            2	          10.0  2010-01-06	   39
            3	          10.0  2010-01-07	   39
            4	          10.0  2010-01-08     39
            ...	           ...         ...    ...
            15095         55.0  2015-12-24	   29
            15096         55.0  2015-12-28	   29
            15097         55.0  2015-12-29	   29
            15098         55.0  2015-12-30	   29
            15099         55.0  2015-12-31	   29
        """
        ...

    @group_operation
    def group_median(self, group):
        """
        Median of the values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group median timeseries of the PrismComponent

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # data component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_median(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31')
                   GICS sector        date	   value
            0	          10.0  2010-01-04	0.205486
            1	          10.0	2010-01-05	0.257924
            2	          10.0  2010-01-06	0.326705
            3	          10.0  2010-01-07	0.329350
            4	          10.0  2010-01-08	0.390691
            ...	           ...         ...	     ...
            15095         55.0  2015-12-24	0.061547
            15096         55.0  2015-12-28	0.064403
            15097         55.0  2015-12-29	0.085882
            15098         55.0  2015-12-30	0.079646
            15099         55.0  2015-12-31	0.080636
        """
        ...

    @group_operation
    def group_demean(self, group):
        """
        Demeaned of values over across each date and group for each element.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group demean timeseries of the PrismComponent

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # data component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_demean(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  -0.000867     AFL
            1         2586086  2010-01-05   0.023705     AFL
            2         2586086  2010-01-06   0.040230     AFL
            3         2586086  2010-01-07   0.018340     AFL
            4         2586086  2010-01-08   0.003084     AFL
            ...           ...         ...        ...     ...
            755337  344286611  2011-10-25  -0.065807     ITT
            755338  344286611  2011-10-26  -0.081308     ITT
            755339  344286611  2011-10-27  -0.121696     ITT
            755340  344286611  2011-10-28  -0.104128     ITT
            755341  344286611  2011-10-31  -0.065463     ITT
        """
        ...

    @group_operation
    def group_z_score(self, group):
        """
        Z-score of the values over across each date and group for each element.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group z-score timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # data component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_z_score(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])\
                    listingid        date      value  Ticker
            0         2586086  2010-01-04  -0.015607     AFL
            1         2586086  2010-01-05   0.421663     AFL
            2         2586086  2010-01-06   0.754689     AFL
            3         2586086  2010-01-07   0.282194     AFL
            4         2586086  2010-01-08   0.051700     AFL
            ...           ...         ...        ...     ...
            755337  344286611  2011-10-25  -0.891504     ITT
            755338  344286611  2011-10-26  -1.087371     ITT
            755339  344286611  2011-10-27  -1.296089     ITT
            755340  344286611  2011-10-28  -1.136280     ITT
            755341  344286611  2011-10-31  -0.707442     ITT
        """
        ...

    @_validate_args
    @group_operation
    def group_rank(self, group, rank_method: str = "standard", ascending: bool = True):
        """
        Ranks of values (1 through n) across each date and group for each element.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

            rank_method : str {'standard', 'modified', 'dense', 'ordinal', 'fractional'}, default 'standard'
                | Method for how equal values are assigned a rank.

                - standard: 1 2 2 4
                - modified: 1 3 3 4
                - dense: 1 2 2 3
                - ordinal: 1 2 3 4
                - fractional: 1 2.5 2.5 4

            ascending : bool, default True
                Whether or not the elements should be ranked in ascending order.

        Returns
        -------
            prism._PrismComponent
                Group ranking of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # data component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_rank(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04   35.0     AFL
            1         2586086  2010-01-05   52.0     AFL
            2         2586086  2010-01-06   61.0     AFL
            3         2586086  2010-01-07   51.0     AFL
            4         2586086  2010-01-08   40.0     AFL
            ...           ...         ...    ...     ...
            755337  344286611  2011-10-25   10.0     ITT
            755338  344286611  2011-10-26    6.0     ITT
            755339  344286611  2011-10-27    6.0     ITT
            755340  344286611  2011-10-28    8.0     ITT
            755341  344286611  2011-10-31   15.0     ITT
        """
        ...

    @_validate_args
    @group_operation
    def group_percentile(self, group, rank_method: str = "standard", ascending: bool = True):
        """
        Percentile of values (between 0 and 1) across each date and group for each element.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

            rank_method : str {'standard', 'modified', 'dense', 'ordinal', 'fractional'}, default 'standard'
                | Method for how equal values are assigned a rank.

                - standard: 1 2 2 4
                - modified: 1 3 3 4
                - dense: 1 2 2 3
                - ordinal: 1 2 3 4
                - fractional: 1 2.5 2.5 4

            ascending : bool, default True
                Whether or not the elements should be ranked in ascending order.

        Returns
        -------
            prism._PrismComponent
                Group percentile timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # data component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_percentile(gics_sector) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  value  Ticker
            0         2586086  2010-01-04    3.0     AFL
            1         2586086  2010-01-05    4.0     AFL
            2         2586086  2010-01-06    4.0     AFL
            3         2586086  2010-01-07    4.0     AFL
            4         2586086  2010-01-08    3.0     AFL
            ...           ...         ...    ...     ...
            755337  344286611  2011-10-25    5.0     ITT
            755338  344286611  2011-10-26    5.0     ITT
            755339  344286611  2011-10-27    5.0     ITT
            755340  344286611  2011-10-28    5.0     ITT
            755341  344286611  2011-10-31    2.0     ITT
        """
        ...

    @_validate_args
    @group_operation
    def group_quantile(
        self,
        group,
        bins: int,
        rank_method: str = "standard",
        ascending: bool = True,
        right: bool = True,
    ):
        """
        Quantile of values across each date and group for each element.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

            bins : int
                Number of quantiles. 10 for deciles, 4 for quartiles, etc.

            rank_method : str {'standard', 'modified', 'dense', 'ordinal', 'fractional'}, default 'standard'
                | Method for how equal values are assigned a rank.

                - standard: 1 2 2 4
                - modified: 1 3 3 4
                - dense: 1 2 2 3
                - ordinal: 1 2 3 4
                - fractional: 1 2.5 2.5 4

            ascending : bool, default True
                Whether or not the elements should be ranked in ascending order.

            right: bool, default True
                | If True, given a border value in between bins, whether to put the sample in the which bins.
                | For example, if the value borders for bin 1 is between 0 ~ 5 and bin 2 is between 5 ~ 10, if right is True, and a sample has a value 5, then it will be assigned bin 1. if False, then bin 2.

        Returns
        -------
            prism._PrismComponent
                Group percentile timeseries of the PrismComponent.

        Examples
        --------
            >>> close = prism.market.close()
            >>> close.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date  Close  Ticker
            0         2586086  2010-01-04  47.57     AFL
            1         2586086  2010-01-05  48.95     AFL
            2         2586086  2010-01-06  49.38     AFL
            3         2586086  2010-01-07  49.91     AFL
            4         2586086  2010-01-08  49.41     AFL
            ...           ...         ...    ...     ...
            755971  344286611  2011-10-25  44.02     ITT
            755972  344286611  2011-10-26  43.54     ITT
            755973  344286611  2011-10-27  44.31     ITT
            755974  344286611  2011-10-28  44.99     ITT
            755975  344286611  2011-10-31  45.60     ITT

            # look for GICS Sector Security Master attribute to create a group
            >>> prism.securitymaster.list_attribute()
            ['Trading Item ID',
            'VALOR',
            'GVKEY',
            'MarkIt Red Code',
            'Country',
            'GICS Sector',
            'WKN',
            'CINS',
            "Moody's Issuer Number",
            'GICS Group',
            'SEDOL',
            'Company Name',
            'CMA Entity ID',
            'CIQ Primary',
            'NAICS',
            'Factset Security ID',
            'Composite FIGI',
            'Share Class FIGI',
            'FIGI',
            'Compustat Primary',
            'Factset Company ID',
            'Ticker',
            'Factset Entity ID',
            'GVKEYIID',
            'Company ID',
            'Factset Listing ID',
            'LEI',
            'IBES Ticker',
            'CUSIP',
            'GICS Sub-Industry',
            'Barra ID',
            'ISIN',
            'MIC',
            'SIC',
            'Security ID',
            'Trade Currency',
            'GICS Industry',
            'Fitch Issuer ID',
            'RatingsXpress Entity ID',
            'SNL Institution ID']

            >>> gics_sector = prism.securitymaster.attribute('GICS Sector') # data component: GICS Sector
            >>> close_result = close.n_periods_pct_change(21).group_quantile(gics_sector, 5) # trading month momentum group ranking on gics sector
            >>> close_result.get_data(universe='S&P 500', startdate='2010-01-01', enddate='2015-12-31', shownid=['ticker'])
                    listingid        date     value  Ticker
            0         2586086  2010-01-04  0.448718     AFL
            1         2586086  2010-01-05  0.666667     AFL
            2         2586086  2010-01-06  0.782051     AFL
            3         2586086  2010-01-07  0.653846     AFL
            4         2586086  2010-01-08  0.512821     AFL
            ...           ...         ...       ...     ...
            755337  344286611  2011-10-25  0.166667     ITT
            755338  344286611  2011-10-26  0.100000     ITT
            755339  344286611  2011-10-27  0.100000     ITT
            755340  344286611  2011-10-28  0.133333     ITT
            755341  344286611  2011-10-31  0.250000     ITT
        """
        ...

    @group_operation
    def group_mode(self, group):
        """
        Mode of the values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group mode timeseries of the PrismComponent.

        Examples
        --------
        TODO
        """
        ...

    @group_operation
    def group_skew(self, group):
        """
        Skewness values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group skewness timeseries of the PrismComponent.

        Examples
        --------
        TODO
        """
        ...

    @group_operation
    def group_kurt(self, group):
        """
        Kurtosis values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group kurtosis timeseries of the PrismComponent.

        Examples
        --------
        TODO
        """
        ...

    @group_operation
    def group_prod(self, group):
        """
        Product values over across each date and group.

        Parameters
        ----------
            group : PrismComponent
                Used to determine the groups.

        Returns
        -------
            prism._PrismComponent
                Group product timeseries of the PrismComponent.

        Examples
        --------
        TODO
        """
        ...

    # map operation
    @_validate_args
    def map(self, args: dict):
        """
        Map values of Component according to an input mapping or function.
        Used for substituting each value in a Component with another value, that may be derived from a function, a ``dict`` .

        Parameters
        ----------
            args : dict

        Returns
        -------
            prism._PrismComponent
                Resampled timeseries of the PrismComponent.

        Examples
        --------
            Winsorization Example

            >>> # Create Earnings to Price Z score
            >>> ni = prism.financial.income_statement(dataitemid=100639, periodtype='LTM')
            >>> mcap = prism.market.market_cap()
            >>> ep = ni.resample('D') / mcap
            >>> ep_z = ep.cross_sectional_z_score()
            >>> ep_z.get_data(1, startdate='2010-01-01')
                    listingid       date     marketcap
            0         38593288  2010-01-01  -340.182838
            1         20221860  2010-01-01   -40.071622
            2         20168002  2010-01-01    -3.852210
            3         31780211  2010-01-01    -0.998875
            4         31778710  2010-01-01    -0.967982
            ...            ...         ...          ...
            8047487   20219090  2022-11-01     0.657311
            8047488  243257057  2022-11-01     1.000056
            8047489   20215516  2022-11-01     1.609253
            8047490   20459086  2022-11-01    57.791387

            >>> # Apply Winsorization
            >>> ep_z_wind = (ep_z < -3).map({True: -3, False: ep_z})
            >>> ep_z_wind.get_data(1, startdate='2010-01-01')
                    listingid       date   marketcap
            0         38593288  2010-01-01  -3.000000
            1         20221860  2010-01-01  -3.000000
            2         20168002  2010-01-01  -3.000000
            3         38593288  2010-01-02  -3.000000
            4         20221860  2010-01-02  -3.000000
            ...            ...         ...        ...
            8047487   20219090  2022-11-01   0.657311
            8047488  243257057  2022-11-01   1.000056
            8047489   20215516  2022-11-01   1.609253
            8047490   20459086  2022-11-01  57.791387
        """
        component_args = {}
        children = [self._query]

        for k, v in args.items():
            if isinstance(v, _PrismComponent):
                # nodeid = str(uuid.uuid4())
                query = copy.deepcopy(v._query)
                # query['nodeid'] = nodeid
            else:
                query = {
                    "component_type": PrismComponentType.DATA_COMPONENT,
                    "component_name": OtherDataComponentType.PRISMVALUE,
                    "component_args": {"data": SPECIALVALUEMAP.get(v, v)},
                    "children": [],
                    "nodeid": str(uuid.uuid4()),
                }
            component_args[k] = query
            children.append(query)

        query = {
            "component_type": PrismComponentType.FUNCTION_COMPONENT,
            "component_name": "map",
            "component_args": component_args,
            "children": children,
            "nodeid": str(uuid.uuid4()),
        }

        ret = _PrismComponent(**query)
        return ret


class _PrismDataComponent(_AbstractPrismComponent):
    """
    Abstract class for base nodes.
    Enforces _component_name as default class attribute.
    Args:
        kwargs: dict of component_args
    """

    _component_type = PrismComponentType.DATA_COMPONENT

    def __init__(self, **kwargs):
        component_args = dict(kwargs)
        query = {
            "component_type": self._component_type,
            "component_category": self._component_category,
            "component_name": self._component_name,
            "component_args": component_args,
            "children": [],
            "nodeid": str(uuid.uuid4()),
        }
        val_res = requests.post(url=URL_DATAQUERIES + "/validate", json=query, headers=_authentication())
        if val_res.status_code >= 400:
            if val_res.status_code == 401:
                raise PrismAuthError(f"Please Login First")
            else:
                try:
                    err_msg = val_res.json()["message"]
                except:
                    err_msg = val_res.content
                raise PrismResponseError(err_msg)
        query = val_res.json()["rescontent"]["data"]
        query.pop("query_name")
        super().__init__(**query)

    @property
    @classmethod
    @abstractmethod
    def _component_name():
        raise NotImplementedError()


    @property
    @classmethod
    @abstractmethod
    def _component_category():
        raise NotImplementedError()


    def __setattr__(self, name, value):
        if name == "_component_name":
            raise AttributeError("Can't modify {}".format(name))

        if name == "_component_category":
            raise AttributeError("Can't modify {}".format(name))

        super().__setattr__(name, value)


class _PrismTaskComponent(_AbstractPrismComponent, ABC):
    _component_type = PrismComponentType.TASK_COMPONENT

    def __init__(self, **kwargs):
        component_args = dict(kwargs)
        query = {
            "component_type": self._component_type,
            "component_name": self._component_name,
            "component_args": component_args,
            "children": [],
        }
        super().__init__(**query)

    def run(self, *args, **kwargs):
        raise NotImplementedError()

    @_validate_args
    def save(self, name: str) -> None:
        return _taskquery.save_taskquery(self, name)

    @_validate_args
    def extract(self, return_code=False):
        return _taskquery.extract_taskquery(self, return_code)


class _PrismValue(_AbstractPrismComponent):
    _component_type = PrismComponentType.DATA_COMPONENT
    _component_name = OtherDataComponentType.PRISMVALUE

    def __init__(self, **kwargs):
        component_args = dict(kwargs)
        query = {
            "component_type": self._component_type,
            "component_name": self._component_name,
            "component_args": component_args,
            "children": [],
        }
        super().__init__(**query)


class _PrismFinancialComponent(_PrismComponent):

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_max(self, n: int, weights: list = None):
        """
        Return the maximum of the values over given fiscal quarter n.

        Parameters
        ----------
            n : int
                Fiscal quarters for calculating maximum values, accepts negative values.

            min_periods : int, default 1
                Minimum number of fiscal quarters required to have a value; otherwise, result is ``np.nan``.

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n fiscal quarters maximum timeseries of the PrismFinancialComponent.
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_min(self, n: int, weights: list = None):
        """
        Minimum of the values over given fiscal quarter n.

        Parameters
        ----------
            n : int
                Fiscal quarters for calculating minimum values, accepts negative values.

            min_periods : int, default 1
                Minimum number of fiscal quarters required to have a value; otherwise, result is ``np.nan``.

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied element-wise with the values in the window.

        Returns
        -------
            prism._PrismComponent
                n fiscal quarters minimum timeseries of the PrismFinancialComponent.
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_shift(self, n: int):
        """
        Shift elements by n fiscal quarters.

        Parameters
        ----------
            n : int
                Number of fiscal quarters to shift. Can be positive or negative.

        Returns
        -------
            prism._PrismComponent
                Shifted values of the PrismFinancialComponent.
        """
        ...

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_diff(self, n: int):
        """
        Difference of a PrismFinancialComponent element compared with another element in the PrismFinancialComponent (default is element in previous fiscal quarter).

        Parameters
        ----------
            n : int
                Fiscal quarters to shift for calculating difference, accepts negative values.

        Returns
        -------
            prism._PrismComponent
                First differences of the PrismFinancialComponent.
        """
        ...

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_pct_change(self, n: int, positive_denominator: bool = False):
        """
        Percentage change between the current and a prior fiscal quarter element. Computes the percentage change from the immediately previous fiscal quarter by default.

        Parameters
        ----------
            n : int
                Fiscal quarters to shift for calculating percent change, accepts negative values.

            positive_denominator: bool, default False
                Whether to only include result of positive denominator. The result from negative or zero denominator will be assigned ``Numpy.nan``

        Returns
        -------
            prism._PrismComponent
                Percent change of the PrismFinancialComponent.
        """
        ...


    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_mean(self, n: int, weights: list = None):
        """
        Mean of the values over given fiscal quarters n.

        Parameters
        ----------
            n : int
                Fiscal quarters for calculating mean values, accepts negative values.

            min_periods : int, default 1
                Minimum number of fiscal quarters required to have a value; otherwise, result is ``np.nan``.

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied elementwise with the values in the window.

        Returns
        -------
            prism._PrismFinancialComponent
                n fiscal quarters mean timeseries of the PrismFinancialComponent.
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_std(self, n: int, weights: list = None):
        """
        Standard deviation of the values over given fiscal quarters n.

        Parameters
        ----------
            n : int
                Fiscal quarters for calculating standard deviation values, accepts negative values.

            min_periods : int, default 1
                Minimum number of fiscal quarters required to have a value; otherwise, result is ``np.nan``.

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied elementwise with the values in the window.

        Returns
        -------
            prism._PrismFinancialComponent
                n fiscal quarters standard deviation timeseries of the PrismFinancialComponent.
        """

        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_var(self, n: int, weights: list = None):
        """
        Variance of the values over given fiscal quarters n.

        Parameters
        ----------
            n : int
                Fiscal quarters for calculating variance values, accepts negative values.

            min_periods : int, default 1
                Minimum number of fiscal quarters required to have a value; otherwise, result is ``np.nan``.

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied elementwise with the values in the window.

        Returns
        -------
            prism._PrismFinancialComponent
                n fiscal quarters variance timeseries of the PrismFinancialComponent.
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_skew(self, n: int, weights: list = None):
        """
        Skewness of the values over given fiscal quarters n.

        Parameters
        ----------
            n : int
                Fiscal quarters for calculating skewness values, accepts negative values.

            min_periods : int, default 1
                Minimum number of fiscal quarters required to have a value; otherwise, result is ``np.nan``.

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied elementwise with the values in the window.

        Returns
        -------
            prism._PrismFinancialComponent
                n fiscal quarters skewness timeseries of the PrismFinancialComponent.
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_z_score(self, n: int):
        """
        Z-score of the values over given fiscal quarters n.

        Parameters
        ----------
            n : int
                Fiscal quarters for calculating z-score values, accepts negative values.

            min_periods : int, default 1
                Minimum number of fiscal quarters required to have a value; otherwise, result is ``np.nan``.

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied elementwise with the values in the window.

        Returns
        -------
            prism._PrismFinancialComponent
                n fiscal quarters z-score timeseries of the PrismFinancialComponent.

        """
        ...

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_prod(self, n: int):
        """
        Product of the values over given fiscal quarters n.

        Parameters
        ----------
            n : int
                Fiscal quarters for calculating product values, accepts negative values.

            min_periods : int, default 1
                Minimum number of fiscal quarters required to have a value; otherwise, result is ``np.nan``.

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied elementwise with the values in the window.

        Returns
        -------
            prism._PrismFinancialComponent
                n fiscal quarters product timeseries of the PrismFinancialComponent.
        """
        ...

    @_validate_args
    @n_period_operation
    @operation
    def n_fiscal_quarters_sum(self, n: int, weights: list = None):
        """
        Sum of the values over given fiscal quarters n.

        Parameters
        ----------
            n : int
                Fiscal quarters for calculating sum values, accepts negative values.

            min_periods : int, default 1
                Minimum number of fiscal quarters required to have a value; otherwise, result is ``np.nan``.

            weights : list, default None
                An optional slice with the same length as the window that will be multiplied elementwise with the values in the window.

        Returns
        -------
            prism._PrismFinancialComponent
                n fiscal quarters sum timeseries of the PrismFinancialComponent.
        """
        if (weights is not None) and (len(weights) != n):
            raise PrismValueError("Number of weights should equal to n")


class _PrismModelComponent(_PrismComponent):
    _component_type = PrismComponentType.MODEL_COMPONENT

    def __init__(self, **kwargs):
        component_args = dict(kwargs)
        children = [] if "children" not in component_args else component_args.pop("children")
        query = {
            "component_type": self._component_type,
            "component_category": self._component_category,
            "component_name": self._component_name,
            "component_args": component_args,
            "children": children,
            "nodeid": str(uuid.uuid4()),
        }
        val_res = requests.post(url=URL_DATAQUERIES + "/validate", json=query, headers=_authentication())
        if val_res.status_code >= 400:
            if val_res.status_code == 401:
                raise PrismAuthError(f"Please Login First")
            else:
                try:
                    err_msg = val_res.json()["message"]
                except:
                    err_msg = val_res.content
                raise PrismResponseError(err_msg)
        query = val_res.json()["rescontent"]["data"]
        query.pop("query_name")
        super().__init__(**query)
