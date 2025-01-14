﻿"""_2126.py

RollerRibDetail
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ROLLER_RIB_DETAIL = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'RollerRibDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerRibDetail',)


class RollerRibDetail(_0.APIBase):
    """RollerRibDetail

    This is a mastapy class.
    """

    TYPE = _ROLLER_RIB_DETAIL

    def __init__(self, instance_to_wrap: 'RollerRibDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chamfer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Chamfer' is the original name of this property."""

        temp = self.wrapped.Chamfer

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @chamfer.setter
    def chamfer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Chamfer = value

    @property
    def diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Diameter' is the original name of this property."""

        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @diameter.setter
    def diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Diameter = value

    @property
    def height_above_race(self) -> 'float':
        """float: 'HeightAboveRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeightAboveRace

        if temp is None:
            return 0.0

        return temp

    @property
    def layback_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'LaybackAngle' is the original name of this property."""

        temp = self.wrapped.LaybackAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @layback_angle.setter
    def layback_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.LaybackAngle = value

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def nominal_contact_height_above_race(self) -> 'float':
        """float: 'NominalContactHeightAboveRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalContactHeightAboveRace

        if temp is None:
            return 0.0

        return temp

    @property
    def present(self) -> 'bool':
        """bool: 'Present' is the original name of this property."""

        temp = self.wrapped.Present

        if temp is None:
            return False

        return temp

    @present.setter
    def present(self, value: 'bool'):
        self.wrapped.Present = bool(value) if value is not None else False

    @property
    def undercut_axial_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'UndercutAxialAngle' is the original name of this property."""

        temp = self.wrapped.UndercutAxialAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @undercut_axial_angle.setter
    def undercut_axial_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.UndercutAxialAngle = value

    @property
    def undercut_axial_start_offset(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'UndercutAxialStartOffset' is the original name of this property."""

        temp = self.wrapped.UndercutAxialStartOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @undercut_axial_start_offset.setter
    def undercut_axial_start_offset(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.UndercutAxialStartOffset = value

    @property
    def undercut_radial_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'UndercutRadialAngle' is the original name of this property."""

        temp = self.wrapped.UndercutRadialAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @undercut_radial_angle.setter
    def undercut_radial_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.UndercutRadialAngle = value

    @property
    def undercut_radial_start_offset(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'UndercutRadialStartOffset' is the original name of this property."""

        temp = self.wrapped.UndercutRadialStartOffset

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @undercut_radial_start_offset.setter
    def undercut_radial_start_offset(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.UndercutRadialStartOffset = value

    @property
    def undercut_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'UndercutRadius' is the original name of this property."""

        temp = self.wrapped.UndercutRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @undercut_radius.setter
    def undercut_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.UndercutRadius = value
