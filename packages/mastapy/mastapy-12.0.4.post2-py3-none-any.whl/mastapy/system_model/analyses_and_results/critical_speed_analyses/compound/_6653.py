﻿"""_6653.py

CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis
"""


from typing import List

from mastapy.system_model.connections_and_sockets.cycloidal import _2297
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6524
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6610
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis',)


class CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis(_6610.AbstractShaftToMountableComponentConnectionCompoundCriticalSpeedAnalysis):
    """CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'CycloidalDiscPlanetaryBearingConnectionCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2297.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2297.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6524.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis]':
        """List[CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6524.CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis]':
        """List[CycloidalDiscPlanetaryBearingConnectionCriticalSpeedAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
