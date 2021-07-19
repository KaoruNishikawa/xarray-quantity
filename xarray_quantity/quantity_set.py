from typing import Union, Hashable, Dict

import xarray as xr
import astropy.units as u

from .quantity_array import QuantityArray


class QuantitySet(xr.Dataset):

    __slots__ = (
        "_attrs",
        "_cache",
        "_coord_names",
        "_dims",
        "_encoding",
        "_close",
        "_indexes",
        "_variables",
    )

    _unit = {}

    def __init__(self, data_vars, *args, **kwargs):
        super().__init__(data_vars, *args, **kwargs)
        for k, v in data_vars.items():
            try:
                if not isinstance(v.unit, u.Unit):
                    raise TypeError
                unit = {k: v.unit}
                self._unit.update(unit)
            except (AttributeError, TypeError):
                pass

    @property
    def unit(self) -> Dict[str, u.Unit]:
        return self._unit

    @unit.setter
    def unit(self, unit: Dict[str, Union[str, u.Unit]]) -> None:
        self._unit.update(unit)

    # override
    def _construct_dataarray(self, name: Hashable) -> QuantityArray:
        da = super()._construct_dataarray(name)
        try:
            return QuantityArray(da, unit=self._unit[name])
        except KeyError:
            return QuantityArray(da)