﻿"""_2751.py

RootAssemblySystemDeflection
"""


from typing import List

from mastapy.system_model.part_model import _2431
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4078
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2776, _2783, _2667, _2648
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7206
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'RootAssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblySystemDeflection',)


class RootAssemblySystemDeflection(_2648.AssemblySystemDeflection):
    """RootAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'RootAssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2431.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4078.RootAssemblyPowerFlow':
        """RootAssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_inputs(self) -> '_2776.SystemDeflection':
        """SystemDeflection: 'SystemDeflectionInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionInputs

        if temp is None:
            return None

        if _2776.SystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast system_deflection_inputs to SystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_deflection_results(self) -> 'List[_2667.ConcentricPartGroupCombinationSystemDeflectionResults]':
        """List[ConcentricPartGroupCombinationSystemDeflectionResults]: 'ShaftDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
