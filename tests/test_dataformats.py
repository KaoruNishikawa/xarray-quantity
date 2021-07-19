import xarray as xr

from xarray_quantity import QuantityArray, QuantitySet


def test_empty():
    emptyqa = QuantityArray()
    emptyqs = QuantitySet()
    assert not emptyqa.unit
    assert emptyqs.unit == {}


def test_quantity_array():
    qa = QuantityArray(
        [1, 2, 3, 4, 5],
        coords={"idx": [0, 1, 2, 3, 4]},
        dims=["idx"],
        unit="km/s",
    )
    assert qa.unit.to_string() == "km / s"
    assert qa.sel(idx=2).data == 3


def test_quantity_set():
    dataarrays = {
        "da1": QuantityArray([1, 2, 3, 4, 5], unit="km"),
        "da2": QuantityArray([11, 12, 13, 14, 15]),
        "da3": xr.DataArray([111, 112, 113, 114, 115]),
    }
    qs = QuantitySet(dataarrays)
    assert qs.da1.unit.to_string() == "km"
    assert qs.da2.data[0] == 11
    assert qs.da3.data[0] == 111
