﻿"""_2615.py

CompoundAdvancedSystemDeflectionSubAnalysis
"""


from mastapy.system_model.analyses_and_results import _2575
from mastapy._internal.python_net import python_net_import

_COMPOUND_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'CompoundAdvancedSystemDeflectionSubAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CompoundAdvancedSystemDeflectionSubAnalysis',)


class CompoundAdvancedSystemDeflectionSubAnalysis(_2575.CompoundAnalysis):
    """CompoundAdvancedSystemDeflectionSubAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPOUND_ADVANCED_SYSTEM_DEFLECTION_SUB_ANALYSIS

    def __init__(self, instance_to_wrap: 'CompoundAdvancedSystemDeflectionSubAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
