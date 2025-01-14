﻿"""_5971.py

ConceptCouplingHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.part_model.couplings import _2537
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6772
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5982
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'ConceptCouplingHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHarmonicAnalysisOfSingleExcitation',)


class ConceptCouplingHarmonicAnalysisOfSingleExcitation(_5982.CouplingHarmonicAnalysisOfSingleExcitation):
    """ConceptCouplingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    def __init__(self, instance_to_wrap: 'ConceptCouplingHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2537.ConceptCoupling':
        """ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6772.ConceptCouplingLoadCase':
        """ConceptCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
