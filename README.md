# xarray-quantity

[![PyPI](https://img.shields.io/pypi/v/PACKAGENAME.svg?label=PyPI&style=flat-square)](https://pypi.org/pypi/xarray-quantity/)
[![Python](https://img.shields.io/pypi/pyversions/PACKAGENAME.svg?label=Python&color=yellow&style=flat-square)](https://pypi.org/pypi/xarray-quantity/)
[![Test](https://img.shields.io/github/workflow/status/USERNAME/PACKAGENAME/Test?logo=github&label=Test&style=flat-square)](https://github.com/KaoruNishikawa/xarray-quantity/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](LICENSE)

xarray extension which supports astropy quantities.

## Features

This library provides:

- xarray DataArray and Dataset with units.

## Installation

```shell
pip install xarray-quantity
```

## Usage

### QuantityArray

To create a DataArray with units, use `QuantityArray` class. The arguments are compatible with DataArray, except the keyword argument `unit`.

```python
>>> qa = QuantityArray([1, 2, 3, 4, 5], unit="km")
>>> qa.data
[1, 2, 3, 4, 5] km
>>> qa.unit
km
```

### QuantitySet

To create a Dataset with units, use `QuantitySet` class. This class also has compatibility with xarray's Dataset.

```python
>>> arrays = {
...     "qa1": QuantityArray([1, 2, 3, 4, 5], unit="km/s"),
...     "qa2": QuantityArray([11, 12, 13, 14, 15]),
...     "da3": xr.DataArray([111, 112, 113, 114, 115])
... }
>>> qs = QuantitySet(arrays)
>>> qs.qa1.data
[1, 2, 3, 4, 5] km / s
>>> qs.qa2
xarray.QuantityArray 'qa2' (dim_0: 5)
<Quantity [11., 12., 13., 14., 15.] km / s>
Coordinates: (0)
Attributes: (0)
```

---

This library is using [Semantic Versioning](https://semver.org).
