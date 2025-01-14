﻿"""_1300.py

ElectricMachineResultsForLineToLine
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_FOR_LINE_TO_LINE = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'ElectricMachineResultsForLineToLine')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResultsForLineToLine',)


class ElectricMachineResultsForLineToLine(_0.APIBase):
    """ElectricMachineResultsForLineToLine

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_FOR_LINE_TO_LINE

    def __init__(self, instance_to_wrap: 'ElectricMachineResultsForLineToLine.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def line_to_line_terminal_voltage_peak(self) -> 'float':
        """float: 'LineToLineTerminalVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineTerminalVoltagePeak

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_terminal_voltage_rms(self) -> 'float':
        """float: 'LineToLineTerminalVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineTerminalVoltageRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def line_to_line_terminal_voltage_harmonic_distortion(self) -> 'float':
        """float: 'LineToLineTerminalVoltageHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineTerminalVoltageHarmonicDistortion

        if temp is None:
            return 0.0

        return temp

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
