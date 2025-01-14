﻿"""_2168.py

DutyCycleImporter
"""


from typing import List

from mastapy.system_model import _2169, _2173
from mastapy.system_model.analyses_and_results.load_case_groups import _5605
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2428, _2429
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_IMPORTER = python_net_import('SMT.MastaAPI.SystemModel', 'DutyCycleImporter')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCycleImporter',)


class DutyCycleImporter(_0.APIBase):
    """DutyCycleImporter

    This is a mastapy class.
    """

    TYPE = _DUTY_CYCLE_IMPORTER

    def __init__(self, instance_to_wrap: 'DutyCycleImporter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_state_destinations(self) -> 'List[_2169.DutyCycleImporterDesignEntityMatch[_5605.DesignState]]':
        """List[DutyCycleImporterDesignEntityMatch[DesignState]]: 'DesignStateDestinations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignStateDestinations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def duty_cycles_to_import(self) -> 'List[_2173.IncludeDutyCycleOption]':
        """List[IncludeDutyCycleOption]: 'DutyCyclesToImport' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCyclesToImport

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_load_destinations(self) -> 'List[_2169.DutyCycleImporterDesignEntityMatch[_2428.PointLoad]]':
        """List[DutyCycleImporterDesignEntityMatch[PointLoad]]: 'PointLoadDestinations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoadDestinations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_load_destinations(self) -> 'List[_2169.DutyCycleImporterDesignEntityMatch[_2429.PowerLoad]]':
        """List[DutyCycleImporterDesignEntityMatch[PowerLoad]]: 'PowerLoadDestinations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoadDestinations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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
