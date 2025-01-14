﻿"""_1189.py

GearMeshingElementOptions
"""


from typing import List

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_GEAR_MESHING_ELEMENT_OPTIONS = python_net_import('SMT.MastaAPI.Gears.FEModel', 'GearMeshingElementOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshingElementOptions',)


class GearMeshingElementOptions(_0.APIBase):
    """GearMeshingElementOptions

    This is a mastapy class.
    """

    TYPE = _GEAR_MESHING_ELEMENT_OPTIONS

    def __init__(self, instance_to_wrap: 'GearMeshingElementOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def body_elements(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'BodyElements' is the original name of this property."""

        temp = self.wrapped.BodyElements

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @body_elements.setter
    def body_elements(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.BodyElements = value

    @property
    def face_elements(self) -> 'int':
        """int: 'FaceElements' is the original name of this property."""

        temp = self.wrapped.FaceElements

        if temp is None:
            return 0

        return temp

    @face_elements.setter
    def face_elements(self, value: 'int'):
        self.wrapped.FaceElements = int(value) if value is not None else 0

    @property
    def fillet_elements(self) -> 'int':
        """int: 'FilletElements' is the original name of this property."""

        temp = self.wrapped.FilletElements

        if temp is None:
            return 0

        return temp

    @fillet_elements.setter
    def fillet_elements(self, value: 'int'):
        self.wrapped.FilletElements = int(value) if value is not None else 0

    @property
    def profile_elements(self) -> 'int':
        """int: 'ProfileElements' is the original name of this property."""

        temp = self.wrapped.ProfileElements

        if temp is None:
            return 0

        return temp

    @profile_elements.setter
    def profile_elements(self, value: 'int'):
        self.wrapped.ProfileElements = int(value) if value is not None else 0

    @property
    def radial_elements(self) -> 'int':
        """int: 'RadialElements' is the original name of this property."""

        temp = self.wrapped.RadialElements

        if temp is None:
            return 0

        return temp

    @radial_elements.setter
    def radial_elements(self, value: 'int'):
        self.wrapped.RadialElements = int(value) if value is not None else 0

    @property
    def rim_elements(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'RimElements' is the original name of this property."""

        temp = self.wrapped.RimElements

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @rim_elements.setter
    def rim_elements(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.RimElements = value

    @property
    def tip_elements(self) -> 'int':
        """int: 'TipElements' is the original name of this property."""

        temp = self.wrapped.TipElements

        if temp is None:
            return 0

        return temp

    @tip_elements.setter
    def tip_elements(self, value: 'int'):
        self.wrapped.TipElements = int(value) if value is not None else 0

    @property
    def web_elements(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'WebElements' is the original name of this property."""

        temp = self.wrapped.WebElements

        if temp is None:
            return 0

        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else 0

    @web_elements.setter
    def web_elements(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.WebElements = value

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
