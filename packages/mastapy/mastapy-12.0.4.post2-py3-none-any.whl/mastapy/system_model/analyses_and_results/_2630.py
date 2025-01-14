﻿"""_2630.py

CompoundModalAnalysisForHarmonicAnalysis
"""


from mastapy.system_model.analyses_and_results import _2575
from mastapy._internal.python_net import python_net_import

_COMPOUND_MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundModalAnalysisForHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundModalAnalysisForHarmonicAnalysis',)


class CompoundModalAnalysisForHarmonicAnalysis(_2575.CompoundAnalysis):
    """CompoundModalAnalysisForHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_MODAL_ANALYSIS_FOR_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'CompoundModalAnalysisForHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
