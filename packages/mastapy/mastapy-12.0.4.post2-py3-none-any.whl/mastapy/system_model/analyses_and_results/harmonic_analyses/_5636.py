﻿"""_5636.py

BevelDifferentialSunGearHarmonicAnalysis
"""


from mastapy.system_model.part_model.gears import _2474
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2656
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5632
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'BevelDifferentialSunGearHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialSunGearHarmonicAnalysis',)


class BevelDifferentialSunGearHarmonicAnalysis(_5632.BevelDifferentialGearHarmonicAnalysis):
    """BevelDifferentialSunGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'BevelDifferentialSunGearHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2474.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2656.BevelDifferentialSunGearSystemDeflection':
        """BevelDifferentialSunGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
