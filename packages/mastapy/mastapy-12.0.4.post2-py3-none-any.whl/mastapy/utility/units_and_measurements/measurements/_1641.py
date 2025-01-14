﻿"""_1641.py

LinearAngularStiffnessCrossTerm
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_LINEAR_ANGULAR_STIFFNESS_CROSS_TERM = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LinearAngularStiffnessCrossTerm')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearAngularStiffnessCrossTerm',)


class LinearAngularStiffnessCrossTerm(_1573.MeasurementBase):
    """LinearAngularStiffnessCrossTerm

    This is a mastapy class.
    """

    TYPE = _LINEAR_ANGULAR_STIFFNESS_CROSS_TERM

    def __init__(self, instance_to_wrap: 'LinearAngularStiffnessCrossTerm.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
