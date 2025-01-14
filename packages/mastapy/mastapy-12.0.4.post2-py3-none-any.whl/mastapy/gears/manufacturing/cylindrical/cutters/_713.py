﻿"""_713.py

MutatableCurve
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.geometry.two_d.curves import _307
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.manufacturing.cylindrical.cutters import _712
from mastapy._internal.python_net import python_net_import

_MUTATABLE_CURVE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'MutatableCurve')


__docformat__ = 'restructuredtext en'
__all__ = ('MutatableCurve',)


class MutatableCurve(_712.MutatableCommon):
    """MutatableCurve

    This is a mastapy class.
    """

    TYPE = _MUTATABLE_CURVE

    def __init__(self, instance_to_wrap: 'MutatableCurve.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning(self) -> 'float':
        """float: 'Crowning' is the original name of this property."""

        temp = self.wrapped.Crowning

        if temp is None:
            return 0.0

        return temp

    @crowning.setter
    def crowning(self, value: 'float'):
        self.wrapped.Crowning = float(value) if value is not None else 0.0

    @property
    def curve_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes':
        """enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes: 'CurveType' is the original name of this property."""

        temp = self.wrapped.CurveType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @curve_type.setter
    def curve_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BasicCurveTypes.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.CurveType = value

    @property
    def height(self) -> 'float':
        """float: 'Height' is the original name of this property."""

        temp = self.wrapped.Height

        if temp is None:
            return 0.0

        return temp

    @height.setter
    def height(self, value: 'float'):
        self.wrapped.Height = float(value) if value is not None else 0.0

    @property
    def height_end(self) -> 'float':
        """float: 'HeightEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeightEnd

        if temp is None:
            return 0.0

        return temp

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value is not None else 0.0

    @property
    def linear_modification(self) -> 'float':
        """float: 'LinearModification' is the original name of this property."""

        temp = self.wrapped.LinearModification

        if temp is None:
            return 0.0

        return temp

    @linear_modification.setter
    def linear_modification(self, value: 'float'):
        self.wrapped.LinearModification = float(value) if value is not None else 0.0

    @property
    def nominal_section_pressure_angle(self) -> 'float':
        """float: 'NominalSectionPressureAngle' is the original name of this property."""

        temp = self.wrapped.NominalSectionPressureAngle

        if temp is None:
            return 0.0

        return temp

    @nominal_section_pressure_angle.setter
    def nominal_section_pressure_angle(self, value: 'float'):
        self.wrapped.NominalSectionPressureAngle = float(value) if value is not None else 0.0

    @property
    def pressure_angle_modification(self) -> 'float':
        """float: 'PressureAngleModification' is the original name of this property."""

        temp = self.wrapped.PressureAngleModification

        if temp is None:
            return 0.0

        return temp

    @pressure_angle_modification.setter
    def pressure_angle_modification(self, value: 'float'):
        self.wrapped.PressureAngleModification = float(value) if value is not None else 0.0

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value is not None else 0.0
