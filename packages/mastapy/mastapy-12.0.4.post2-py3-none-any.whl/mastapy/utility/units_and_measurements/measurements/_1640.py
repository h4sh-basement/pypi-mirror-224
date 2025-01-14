﻿"""_1640.py

LinearAngularDamping
"""


from mastapy.utility.units_and_measurements import _1573
from mastapy._internal.python_net import python_net_import

_LINEAR_ANGULAR_DAMPING = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'LinearAngularDamping')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearAngularDamping',)


class LinearAngularDamping(_1573.MeasurementBase):
    """LinearAngularDamping

    This is a mastapy class.
    """

    TYPE = _LINEAR_ANGULAR_DAMPING

    def __init__(self, instance_to_wrap: 'LinearAngularDamping.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
