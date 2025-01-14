﻿"""_3278.py

PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft
"""


from mastapy.system_model.part_model.couplings import _2544
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6863
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3235
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft',)


class PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft(_3235.CouplingSteadyStateSynchronousResponseOnAShaft):
    """PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2544.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6863.PartToPartShearCouplingLoadCase':
        """PartToPartShearCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
