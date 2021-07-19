# flake8: noqa

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution("xarray-quantity").version
except pkg_resources.DistributionNotFound:
    __version__ = "0.1.1"

from .quantity_array import QuantityArray
from .quantity_set import QuantitySet
