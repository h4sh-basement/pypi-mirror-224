﻿"""_1612.py

ForcePerUnitPressure
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_FORCE_PER_UNIT_PRESSURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ForcePerUnitPressure')


__docformat__ = 'restructuredtext en'
__all__ = ('ForcePerUnitPressure',)


class ForcePerUnitPressure(_1573.MeasurementBase):
    """ForcePerUnitPressure

    This is a mastapy class.
    """

    TYPE = _FORCE_PER_UNIT_PRESSURE

    def __init__(self, instance_to_wrap: 'ForcePerUnitPressure.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
