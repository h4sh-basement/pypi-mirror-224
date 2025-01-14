﻿"""_1607.py

EnergySmall
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_ENERGY_SMALL = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'EnergySmall')


__docformat__ = 'restructuredtext en'
__all__ = ('EnergySmall',)


class EnergySmall(_1573.MeasurementBase):
    """EnergySmall

    This is a mastapy class.
    """

    TYPE = _ENERGY_SMALL

    def __init__(self, instance_to_wrap: 'EnergySmall.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
