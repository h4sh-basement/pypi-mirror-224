﻿"""_3443.py

TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2563
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3316
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import _3363
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound', 'TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft',)


class TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft(_3363.CouplingCompoundSteadyStateSynchronousResponseOnAShaft):
    """TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    def __init__(self, instance_to_wrap: 'TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2563.TorqueConverter':
        """TorqueConverter: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2563.TorqueConverter':
        """TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3316.TorqueConverterSteadyStateSynchronousResponseOnAShaft]':
        """List[TorqueConverterSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3316.TorqueConverterSteadyStateSynchronousResponseOnAShaft]':
        """List[TorqueConverterSteadyStateSynchronousResponseOnAShaft]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
