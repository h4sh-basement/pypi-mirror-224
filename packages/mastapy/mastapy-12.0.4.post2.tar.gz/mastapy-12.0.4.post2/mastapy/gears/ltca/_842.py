﻿"""_842.py

MeshedGearLoadDistributionAnalysisAtRotation
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.ltca import _838
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_MESHED_GEAR_LOAD_DISTRIBUTION_ANALYSIS_AT_ROTATION = python_net_import('SMT.MastaAPI.Gears.LTCA', 'MeshedGearLoadDistributionAnalysisAtRotation')


__docformat__ = 'restructuredtext en'
__all__ = ('MeshedGearLoadDistributionAnalysisAtRotation',)


class MeshedGearLoadDistributionAnalysisAtRotation(_0.APIBase):
    """MeshedGearLoadDistributionAnalysisAtRotation

    This is a mastapy class.
    """

    TYPE = _MESHED_GEAR_LOAD_DISTRIBUTION_ANALYSIS_AT_ROTATION

    def __init__(self, instance_to_wrap: 'MeshedGearLoadDistributionAnalysisAtRotation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_name(self) -> 'str':
        """str: 'GearName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearName

        if temp is None:
            return ''

        return temp

    @property
    def compression_side_fillet_results(self) -> 'List[_838.GearRootFilletStressResults]':
        """List[GearRootFilletStressResults]: 'CompressionSideFilletResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompressionSideFilletResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tension_side_fillet_results(self) -> 'List[_838.GearRootFilletStressResults]':
        """List[GearRootFilletStressResults]: 'TensionSideFilletResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TensionSideFilletResults

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
