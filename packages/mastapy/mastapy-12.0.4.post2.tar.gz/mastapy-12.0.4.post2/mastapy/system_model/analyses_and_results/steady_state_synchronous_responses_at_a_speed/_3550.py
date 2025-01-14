﻿"""_3550.py

ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2554
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6881
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3491
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed',)


class ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed(_3491.ConnectorSteadyStateSynchronousResponseAtASpeed):
    """ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2554.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6881.ShaftHubConnectionLoadCase':
        """ShaftHubConnectionLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed]':
        """List[ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
