﻿"""_2882.py

PartCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2736
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7476
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'PartCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundSystemDeflection',)


class PartCompoundSystemDeflection(_7476.PartCompoundAnalysis):
    """PartCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'PartCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2736.PartSystemDeflection]':
        """List[PartSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2736.PartSystemDeflection]':
        """List[PartSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
