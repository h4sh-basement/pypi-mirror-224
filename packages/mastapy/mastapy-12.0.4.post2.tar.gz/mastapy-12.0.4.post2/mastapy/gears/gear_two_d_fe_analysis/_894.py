﻿"""_894.py

FindleyCriticalPlaneAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FINDLEY_CRITICAL_PLANE_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.GearTwoDFEAnalysis', 'FindleyCriticalPlaneAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FindleyCriticalPlaneAnalysis',)


class FindleyCriticalPlaneAnalysis(_0.APIBase):
    """FindleyCriticalPlaneAnalysis

    This is a mastapy class.
    """

    TYPE = _FINDLEY_CRITICAL_PLANE_ANALYSIS

    def __init__(self, instance_to_wrap: 'FindleyCriticalPlaneAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crack_initiation_risk_factor(self) -> 'List[float]':
        """List[float]: 'CrackInitiationRiskFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrackInitiationRiskFactor

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def max_normal_stress(self) -> 'List[float]':
        """List[float]: 'MaxNormalStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxNormalStress

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def max_shear_amplitude(self) -> 'List[float]':
        """List[float]: 'MaxShearAmplitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxShearAmplitude

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def maximum_findley_critical_plane_angle(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'MaximumFindleyCriticalPlaneAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumFindleyCriticalPlaneAngle

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, Vector2D)
        return value

    @property
    def maximum_findley_critical_plane_stress(self) -> 'List[float]':
        """List[float]: 'MaximumFindleyCriticalPlaneStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumFindleyCriticalPlaneStress

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value
