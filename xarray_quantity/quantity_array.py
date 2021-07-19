from typing import Any, Union

import xarray as xr
import astropy.units as u


class QuantityArray(xr.DataArray):

    __slots__ = (
        "_cache",
        "_coords",
        "_close",
        "_indexes",
        "_name",
        "_variable",
        "_unit",
    )

    def __init__(self, *args, **kwargs):
        try:
            self._unit = u.Unit(kwargs.pop("unit"))
        except KeyError:
            self._unit = None
        super().__init__(*args, **kwargs)

    @property
    def unit(self) -> u.Unit:
        return self._unit

    @unit.setter
    def unit(self, new_unit: Union[str, u.Unit]) -> None:
        self._unit = u.Unit(new_unit)

    # override
    @property
    def data(self) -> Any:
        if self._unit:
            return self.variable.data << self._unit
        return self.variable.data

    # override
    @data.setter
    def data(self, value: Any) -> None:
        self.variable.data = value
        if isinstance(value, u.Quantity):
            self._unit = value.unit
