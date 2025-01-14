﻿"""_1705.py

WearCoefficient
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_WEAR_COEFFICIENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'WearCoefficient')


__docformat__ = 'restructuredtext en'
__all__ = ('WearCoefficient',)


class WearCoefficient(_1573.MeasurementBase):
    """WearCoefficient

    This is a mastapy class.
    """

    TYPE = _WEAR_COEFFICIENT

    def __init__(self, instance_to_wrap: 'WearCoefficient.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
