﻿"""_3759.py

CycloidalDiscCentralBearingConnectionStabilityAnalysis
"""


from mastapy.system_model.connections_and_sockets.cycloidal import _2294
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3738
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'CycloidalDiscCentralBearingConnectionStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionStabilityAnalysis',)


class CycloidalDiscCentralBearingConnectionStabilityAnalysis(_3738.CoaxialConnectionStabilityAnalysis):
    """CycloidalDiscCentralBearingConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2294.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
