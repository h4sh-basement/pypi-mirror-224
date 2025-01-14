﻿"""_1643.py

LinearFlexibility
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_LINEAR_FLEXIBILITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LinearFlexibility')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearFlexibility',)


class LinearFlexibility(_1573.MeasurementBase):
    """LinearFlexibility

    This is a mastapy class.
    """

    TYPE = _LINEAR_FLEXIBILITY

    def __init__(self, instance_to_wrap: 'LinearFlexibility.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
