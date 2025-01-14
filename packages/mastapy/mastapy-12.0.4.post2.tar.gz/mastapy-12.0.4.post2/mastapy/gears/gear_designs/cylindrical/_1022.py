﻿"""_1022.py

CylindricalGearSetFlankDesign
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_FLANK_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearSetFlankDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetFlankDesign',)


class CylindricalGearSetFlankDesign(_0.APIBase):
    """CylindricalGearSetFlankDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_FLANK_DESIGN

    def __init__(self, instance_to_wrap: 'CylindricalGearSetFlankDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_helix_angle(self) -> 'float':
        """float: 'BaseHelixAngle' is the original name of this property."""

        temp = self.wrapped.BaseHelixAngle

        if temp is None:
            return 0.0

        return temp

    @base_helix_angle.setter
    def base_helix_angle(self, value: 'float'):
        self.wrapped.BaseHelixAngle = float(value) if value is not None else 0.0

    @property
    def flank_name(self) -> 'str':
        """str: 'FlankName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankName

        if temp is None:
            return ''

        return temp

    @property
    def minimum_total_contact_ratio(self) -> 'float':
        """float: 'MinimumTotalContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumTotalContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_transverse_contact_ratio(self) -> 'float':
        """float: 'MinimumTransverseContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_base_pitch(self) -> 'float':
        """float: 'NormalBasePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_base_pitch_set_by_changing_normal_module(self) -> 'float':
        """float: 'NormalBasePitchSetByChangingNormalModule' is the original name of this property."""

        temp = self.wrapped.NormalBasePitchSetByChangingNormalModule

        if temp is None:
            return 0.0

        return temp

    @normal_base_pitch_set_by_changing_normal_module.setter
    def normal_base_pitch_set_by_changing_normal_module(self, value: 'float'):
        self.wrapped.NormalBasePitchSetByChangingNormalModule = float(value) if value is not None else 0.0

    @property
    def normal_base_pitch_set_by_changing_normal_pressure_angle(self) -> 'float':
        """float: 'NormalBasePitchSetByChangingNormalPressureAngle' is the original name of this property."""

        temp = self.wrapped.NormalBasePitchSetByChangingNormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_base_pitch_set_by_changing_normal_pressure_angle.setter
    def normal_base_pitch_set_by_changing_normal_pressure_angle(self, value: 'float'):
        self.wrapped.NormalBasePitchSetByChangingNormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def normal_pressure_angle(self) -> 'float':
        """float: 'NormalPressureAngle' is the original name of this property."""

        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    def normal_pressure_angle(self, value: 'float'):
        self.wrapped.NormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def transverse_base_pitch(self) -> 'float':
        """float: 'TransverseBasePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseBasePitch

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle(self) -> 'float':
        """float: 'TransversePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransversePressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def transverse_pressure_angle_normal_pressure_angle(self) -> 'float':
        """float: 'TransversePressureAngleNormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransversePressureAngleNormalPressureAngle

        if temp is None:
            return 0.0

        return temp
