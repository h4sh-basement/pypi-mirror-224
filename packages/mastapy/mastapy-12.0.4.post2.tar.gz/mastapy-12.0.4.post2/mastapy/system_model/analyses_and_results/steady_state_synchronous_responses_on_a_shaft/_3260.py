﻿"""_3260.py

HypoidGearSteadyStateSynchronousResponseOnAShaft
"""


from mastapy.system_model.part_model.gears import _2490
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6837
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3202
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'HypoidGearSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSteadyStateSynchronousResponseOnAShaft',)


class HypoidGearSteadyStateSynchronousResponseOnAShaft(_3202.AGMAGleasonConicalGearSteadyStateSynchronousResponseOnAShaft):
    """HypoidGearSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    def __init__(self, instance_to_wrap: 'HypoidGearSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2490.HypoidGear':
        """HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6837.HypoidGearLoadCase':
        """HypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
