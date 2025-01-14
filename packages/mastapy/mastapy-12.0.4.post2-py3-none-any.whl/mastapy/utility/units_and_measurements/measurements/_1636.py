﻿"""_1636.py

LengthToTheFourth
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_LENGTH_TO_THE_FOURTH = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LengthToTheFourth')


__docformat__ = 'restructuredtext en'
__all__ = ('LengthToTheFourth',)


class LengthToTheFourth(_1573.MeasurementBase):
    """LengthToTheFourth

    This is a mastapy class.
    """

    TYPE = _LENGTH_TO_THE_FOURTH

    def __init__(self, instance_to_wrap: 'LengthToTheFourth.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
