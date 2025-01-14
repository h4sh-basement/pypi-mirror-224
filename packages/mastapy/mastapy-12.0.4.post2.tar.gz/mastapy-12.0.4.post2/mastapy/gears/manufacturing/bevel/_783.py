﻿"""_783.py

ConicalSetManufacturingAnalysis
"""


from mastapy.gears.analysis import _1218
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MANUFACTURING_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalSetManufacturingAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalSetManufacturingAnalysis',)


class ConicalSetManufacturingAnalysis(_1218.GearSetImplementationAnalysis):
    """ConicalSetManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MANUFACTURING_ANALYSIS

    def __init__(self, instance_to_wrap: 'ConicalSetManufacturingAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
