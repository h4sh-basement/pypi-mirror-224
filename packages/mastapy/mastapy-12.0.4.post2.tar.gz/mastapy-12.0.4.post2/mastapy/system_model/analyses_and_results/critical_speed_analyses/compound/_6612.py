﻿"""_6612.py

AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6481
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6640
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis',)


class AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis(_6640.ConicalGearMeshCompoundCriticalSpeedAnalysis):
    """AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_COMPOUND_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_6481.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]':
        """List[AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6481.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]':
        """List[AGMAGleasonConicalGearMeshCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
