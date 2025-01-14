﻿"""_1685.py

TemperaturePerUnitTime
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_TEMPERATURE_PER_UNIT_TIME = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'TemperaturePerUnitTime')


__docformat__ = 'restructuredtext en'
__all__ = ('TemperaturePerUnitTime',)


class TemperaturePerUnitTime(_1573.MeasurementBase):
    """TemperaturePerUnitTime

    This is a mastapy class.
    """

    TYPE = _TEMPERATURE_PER_UNIT_TIME

    def __init__(self, instance_to_wrap: 'TemperaturePerUnitTime.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
