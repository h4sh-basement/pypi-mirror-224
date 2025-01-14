﻿"""_174.py

EigenvalueOptions
"""


from typing import List

from mastapy.nodal_analysis.dev_tools_analyses import _193
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.nodal_analysis import _77
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_EIGENVALUE_OPTIONS = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'EigenvalueOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('EigenvalueOptions',)


class EigenvalueOptions(_0.APIBase):
    """EigenvalueOptions

    This is a mastapy class.
    """

    TYPE = _EIGENVALUE_OPTIONS

    def __init__(self, instance_to_wrap: 'EigenvalueOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_matrix_type(self) -> '_193.MassMatrixType':
        """MassMatrixType: 'MassMatrixType' is the original name of this property."""

        temp = self.wrapped.MassMatrixType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_193.MassMatrixType)(value) if value is not None else None

    @mass_matrix_type.setter
    def mass_matrix_type(self, value: '_193.MassMatrixType'):
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MassMatrixType = value

    @property
    def maximum_mode_frequency(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumModeFrequency' is the original name of this property."""

        temp = self.wrapped.MaximumModeFrequency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @maximum_mode_frequency.setter
    def maximum_mode_frequency(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumModeFrequency = value

    @property
    def minimum_mode_frequency(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MinimumModeFrequency' is the original name of this property."""

        temp = self.wrapped.MinimumModeFrequency

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @minimum_mode_frequency.setter
    def minimum_mode_frequency(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MinimumModeFrequency = value

    @property
    def mode_frequency_shift(self) -> 'float':
        """float: 'ModeFrequencyShift' is the original name of this property."""

        temp = self.wrapped.ModeFrequencyShift

        if temp is None:
            return 0.0

        return temp

    @mode_frequency_shift.setter
    def mode_frequency_shift(self, value: 'float'):
        self.wrapped.ModeFrequencyShift = float(value) if value is not None else 0.0

    @property
    def mode_input_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ModeInputType':
        """enum_with_selected_value.EnumWithSelectedValue_ModeInputType: 'ModeInputMethod' is the original name of this property."""

        temp = self.wrapped.ModeInputMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ModeInputType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @mode_input_method.setter
    def mode_input_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ModeInputType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ModeInputType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ModeInputMethod = value

    @property
    def number_of_modes(self) -> 'int':
        """int: 'NumberOfModes' is the original name of this property."""

        temp = self.wrapped.NumberOfModes

        if temp is None:
            return 0

        return temp

    @number_of_modes.setter
    def number_of_modes(self, value: 'int'):
        self.wrapped.NumberOfModes = int(value) if value is not None else 0

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
