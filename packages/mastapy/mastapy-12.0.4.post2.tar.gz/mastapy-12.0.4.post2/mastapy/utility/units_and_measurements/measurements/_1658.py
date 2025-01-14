﻿"""_1658.py

Power
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_POWER = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'Power')


__docformat__ = 'restructuredtext en'
__all__ = ('Power',)


class Power(_1573.MeasurementBase):
    """Power

    This is a mastapy class.
    """

    TYPE = _POWER

    def __init__(self, instance_to_wrap: 'Power.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
