﻿"""_1617.py

FuelConsumptionEngine
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_FUEL_CONSUMPTION_ENGINE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'FuelConsumptionEngine')


__docformat__ = 'restructuredtext en'
__all__ = ('FuelConsumptionEngine',)


class FuelConsumptionEngine(_1573.MeasurementBase):
    """FuelConsumptionEngine

    This is a mastapy class.
    """

    TYPE = _FUEL_CONSUMPTION_ENGINE

    def __init__(self, instance_to_wrap: 'FuelConsumptionEngine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
