﻿"""_6684.py

MountableComponentCompoundCriticalSpeedAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6555
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6632
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'MountableComponentCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentCompoundCriticalSpeedAnalysis',)


class MountableComponentCompoundCriticalSpeedAnalysis(_6632.ComponentCompoundCriticalSpeedAnalysis):
    """MountableComponentCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'MountableComponentCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6555.MountableComponentCriticalSpeedAnalysis]':
        """List[MountableComponentCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6555.MountableComponentCriticalSpeedAnalysis]':
        """List[MountableComponentCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
