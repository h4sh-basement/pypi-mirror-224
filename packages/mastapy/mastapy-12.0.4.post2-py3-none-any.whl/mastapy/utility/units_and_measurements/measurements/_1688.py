﻿"""_1688.py

ThermalExpansionCoefficient
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_THERMAL_EXPANSION_COEFFICIENT = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ThermalExpansionCoefficient')


__docformat__ = 'restructuredtext en'
__all__ = ('ThermalExpansionCoefficient',)


class ThermalExpansionCoefficient(_1573.MeasurementBase):
    """ThermalExpansionCoefficient

    This is a mastapy class.
    """

    TYPE = _THERMAL_EXPANSION_COEFFICIENT

    def __init__(self, instance_to_wrap: 'ThermalExpansionCoefficient.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
