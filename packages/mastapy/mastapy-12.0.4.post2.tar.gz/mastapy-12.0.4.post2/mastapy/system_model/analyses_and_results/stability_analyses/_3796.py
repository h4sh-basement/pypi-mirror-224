﻿"""_3796.py

PartToPartShearCouplingHalfStabilityAnalysis
"""


from mastapy.system_model.part_model.couplings import _2545
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6862
from mastapy.system_model.analyses_and_results.stability_analyses import _3752
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'PartToPartShearCouplingHalfStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHalfStabilityAnalysis',)


class PartToPartShearCouplingHalfStabilityAnalysis(_3752.CouplingHalfStabilityAnalysis):
    """PartToPartShearCouplingHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHalfStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2545.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6862.PartToPartShearCouplingHalfLoadCase':
        """PartToPartShearCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
