﻿"""_1000.py

CylindricalGearAbstractRackFlank
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import (
    _999, _1001, _1016, _1068,
    _1005, _1034
)
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ABSTRACT_RACK_FLANK = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearAbstractRackFlank')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearAbstractRackFlank',)


class CylindricalGearAbstractRackFlank(_0.APIBase):
    """CylindricalGearAbstractRackFlank

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ABSTRACT_RACK_FLANK

    def __init__(self, instance_to_wrap: 'CylindricalGearAbstractRackFlank.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def chamfer_angle(self) -> 'float':
        """float: 'ChamferAngle' is the original name of this property."""

        temp = self.wrapped.ChamferAngle

        if temp is None:
            return 0.0

        return temp

    @chamfer_angle.setter
    def chamfer_angle(self, value: 'float'):
        self.wrapped.ChamferAngle = float(value) if value is not None else 0.0

    @property
    def chamfer_angle_in_transverse_plane(self) -> 'float':
        """float: 'ChamferAngleInTransversePlane' is the original name of this property."""

        temp = self.wrapped.ChamferAngleInTransversePlane

        if temp is None:
            return 0.0

        return temp

    @chamfer_angle_in_transverse_plane.setter
    def chamfer_angle_in_transverse_plane(self, value: 'float'):
        self.wrapped.ChamferAngleInTransversePlane = float(value) if value is not None else 0.0

    @property
    def diameter_chamfer_height(self) -> 'float':
        """float: 'DiameterChamferHeight' is the original name of this property."""

        temp = self.wrapped.DiameterChamferHeight

        if temp is None:
            return 0.0

        return temp

    @diameter_chamfer_height.setter
    def diameter_chamfer_height(self, value: 'float'):
        self.wrapped.DiameterChamferHeight = float(value) if value is not None else 0.0

    @property
    def edge_radius(self) -> 'float':
        """float: 'EdgeRadius' is the original name of this property."""

        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

    @edge_radius.setter
    def edge_radius(self, value: 'float'):
        self.wrapped.EdgeRadius = float(value) if value is not None else 0.0

    @property
    def edge_radius_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'EdgeRadiusFactor' is the original name of this property."""

        temp = self.wrapped.EdgeRadiusFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @edge_radius_factor.setter
    def edge_radius_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.EdgeRadiusFactor = value

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
    def protuberance_angle(self) -> 'float':
        """float: 'ProtuberanceAngle' is the original name of this property."""

        temp = self.wrapped.ProtuberanceAngle

        if temp is None:
            return 0.0

        return temp

    @protuberance_angle.setter
    def protuberance_angle(self, value: 'float'):
        self.wrapped.ProtuberanceAngle = float(value) if value is not None else 0.0

    @property
    def protuberance_height(self) -> 'float':
        """float: 'ProtuberanceHeight' is the original name of this property."""

        temp = self.wrapped.ProtuberanceHeight

        if temp is None:
            return 0.0

        return temp

    @protuberance_height.setter
    def protuberance_height(self, value: 'float'):
        self.wrapped.ProtuberanceHeight = float(value) if value is not None else 0.0

    @property
    def protuberance_height_factor(self) -> 'float':
        """float: 'ProtuberanceHeightFactor' is the original name of this property."""

        temp = self.wrapped.ProtuberanceHeightFactor

        if temp is None:
            return 0.0

        return temp

    @protuberance_height_factor.setter
    def protuberance_height_factor(self, value: 'float'):
        self.wrapped.ProtuberanceHeightFactor = float(value) if value is not None else 0.0

    @property
    def protuberance_specification(self) -> 'CylindricalGearAbstractRackFlank.ProtuberanceSpecificationMethod':
        """ProtuberanceSpecificationMethod: 'ProtuberanceSpecification' is the original name of this property."""

        temp = self.wrapped.ProtuberanceSpecification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(CylindricalGearAbstractRackFlank.ProtuberanceSpecificationMethod)(value) if value is not None else None

    @protuberance_specification.setter
    def protuberance_specification(self, value: 'CylindricalGearAbstractRackFlank.ProtuberanceSpecificationMethod'):
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ProtuberanceSpecification = value

    @property
    def rack_undercut_clearance(self) -> 'float':
        """float: 'RackUndercutClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RackUndercutClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def rack_undercut_clearance_normal_module(self) -> 'float':
        """float: 'RackUndercutClearanceNormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RackUndercutClearanceNormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_chamfer_height(self) -> 'float':
        """float: 'RadialChamferHeight' is the original name of this property."""

        temp = self.wrapped.RadialChamferHeight

        if temp is None:
            return 0.0

        return temp

    @radial_chamfer_height.setter
    def radial_chamfer_height(self, value: 'float'):
        self.wrapped.RadialChamferHeight = float(value) if value is not None else 0.0

    @property
    def radial_chamfer_height_factor(self) -> 'float':
        """float: 'RadialChamferHeightFactor' is the original name of this property."""

        temp = self.wrapped.RadialChamferHeightFactor

        if temp is None:
            return 0.0

        return temp

    @radial_chamfer_height_factor.setter
    def radial_chamfer_height_factor(self, value: 'float'):
        self.wrapped.RadialChamferHeightFactor = float(value) if value is not None else 0.0

    @property
    def residual_fillet_undercut(self) -> 'float':
        """float: 'ResidualFilletUndercut' is the original name of this property."""

        temp = self.wrapped.ResidualFilletUndercut

        if temp is None:
            return 0.0

        return temp

    @residual_fillet_undercut.setter
    def residual_fillet_undercut(self, value: 'float'):
        self.wrapped.ResidualFilletUndercut = float(value) if value is not None else 0.0

    @property
    def residual_fillet_undercut_factor(self) -> 'float':
        """float: 'ResidualFilletUndercutFactor' is the original name of this property."""

        temp = self.wrapped.ResidualFilletUndercutFactor

        if temp is None:
            return 0.0

        return temp

    @residual_fillet_undercut_factor.setter
    def residual_fillet_undercut_factor(self, value: 'float'):
        self.wrapped.ResidualFilletUndercutFactor = float(value) if value is not None else 0.0

    @property
    def rough_protuberance(self) -> 'float':
        """float: 'RoughProtuberance' is the original name of this property."""

        temp = self.wrapped.RoughProtuberance

        if temp is None:
            return 0.0

        return temp

    @rough_protuberance.setter
    def rough_protuberance(self, value: 'float'):
        self.wrapped.RoughProtuberance = float(value) if value is not None else 0.0

    @property
    def rough_protuberance_factor(self) -> 'float':
        """float: 'RoughProtuberanceFactor' is the original name of this property."""

        temp = self.wrapped.RoughProtuberanceFactor

        if temp is None:
            return 0.0

        return temp

    @rough_protuberance_factor.setter
    def rough_protuberance_factor(self, value: 'float'):
        self.wrapped.RoughProtuberanceFactor = float(value) if value is not None else 0.0

    @property
    def cutter(self) -> '_999.CylindricalGearAbstractRack':
        """CylindricalGearAbstractRack: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _999.CylindricalGearAbstractRack.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to CylindricalGearAbstractRack. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_of_type_cylindrical_gear_basic_rack(self) -> '_1001.CylindricalGearBasicRack':
        """CylindricalGearBasicRack: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _1001.CylindricalGearBasicRack.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to CylindricalGearBasicRack. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_of_type_cylindrical_gear_pinion_type_cutter(self) -> '_1016.CylindricalGearPinionTypeCutter':
        """CylindricalGearPinionTypeCutter: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _1016.CylindricalGearPinionTypeCutter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to CylindricalGearPinionTypeCutter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_of_type_standard_rack(self) -> '_1068.StandardRack':
        """StandardRack: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _1068.StandardRack.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to StandardRack. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear(self) -> '_1005.CylindricalGearDesign':
        """CylindricalGearDesign: 'Gear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gear

        if temp is None:
            return None

        if _1005.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result
