﻿"""_6256.py

CycloidalDiscDynamicAnalysis
"""


from mastapy.system_model.part_model.cycloidal import _2525
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6791
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6212
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'CycloidalDiscDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscDynamicAnalysis',)


class CycloidalDiscDynamicAnalysis(_6212.AbstractShaftDynamicAnalysis):
    """CycloidalDiscDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_DYNAMIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'CycloidalDiscDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2525.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6791.CycloidalDiscLoadCase':
        """CycloidalDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
