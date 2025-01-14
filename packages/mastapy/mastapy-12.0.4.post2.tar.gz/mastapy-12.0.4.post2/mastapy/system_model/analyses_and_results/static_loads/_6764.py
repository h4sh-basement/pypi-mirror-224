﻿"""_6764.py

BoltLoadCase
"""


from mastapy.system_model.part_model import _2399
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6769
from mastapy._internal.python_net import python_net_import

_BOLT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BoltLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltLoadCase',)


class BoltLoadCase(_6769.ComponentLoadCase):
    """BoltLoadCase

    This is a mastapy class.
    """

    TYPE = _BOLT_LOAD_CASE

    def __init__(self, instance_to_wrap: 'BoltLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2399.Bolt':
        """Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
