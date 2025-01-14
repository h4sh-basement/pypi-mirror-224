﻿"""_5349.py

ConceptCouplingHalfMultibodyDynamicsAnalysis
"""


from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2538
from mastapy.system_model.analyses_and_results.static_loads import _6771
from mastapy.system_model.analyses_and_results.mbd_analyses import _5360
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ConceptCouplingHalfMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfMultibodyDynamicsAnalysis',)


class ConceptCouplingHalfMultibodyDynamicsAnalysis(_5360.CouplingHalfMultibodyDynamicsAnalysis):
    """ConceptCouplingHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self) -> '_2538.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6771.ConceptCouplingHalfLoadCase':
        """ConceptCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
