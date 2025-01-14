﻿"""_183.py

FEModelModalAnalysisDrawStyle
"""


from mastapy.nodal_analysis.dev_tools_analyses import _187
from mastapy._internal.python_net import python_net_import

_FE_MODEL_MODAL_ANALYSIS_DRAW_STYLE = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModelModalAnalysisDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModelModalAnalysisDrawStyle',)


class FEModelModalAnalysisDrawStyle(_187.FEModelTabDrawStyle):
    """FEModelModalAnalysisDrawStyle

    This is a mastapy class.
    """

    TYPE = _FE_MODEL_MODAL_ANALYSIS_DRAW_STYLE

    def __init__(self, instance_to_wrap: 'FEModelModalAnalysisDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
