"""
NumPy ufuncs and utilities.
"""

from ._logfact import logfactorial
from ._issnan import issnan
from ._cross import cross3, cross2
from ._first import argfirst, _LT, _LE, _EQ, _NE, _GT, _GE
from ._searchsorted import searchsortedl, searchsortedr
from ._peaktopeak import peaktopeak
from ._minmax import minmax, argminmax, min_argmin, max_argmax
from ._means import gmean, hmean
from ._meanvar import meanvar
from ._mad import mad, mad1, rmad, rmad1
from ._vnorm import vnorm
from ._backlash import backlash
from ._deadzone import deadzone
from ._hysteresis_relay import hysteresis_relay
from ._all_same import all_same
from ._gendot_wrap import gendot
from ._ufunc_inspector import ufunc_inspector

import numpy as _np


class op:
    """
    Allowed values for the `op` argument of `argfirst`.
    """
    LT = _np.int8(_LT)
    LE = _np.int8(_LE)
    EQ = _np.int8(_EQ)
    NE = _np.int8(_NE)
    GT = _np.int8(_GT)
    GE = _np.int8(_GE)
