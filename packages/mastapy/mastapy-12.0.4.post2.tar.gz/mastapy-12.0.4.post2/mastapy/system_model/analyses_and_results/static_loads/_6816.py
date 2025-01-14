﻿"""_6816.py

FaceGearLoadCase
"""


from mastapy.system_model.part_model.gears import _2484
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6822
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearLoadCase',)


class FaceGearLoadCase(_6822.GearLoadCase):
    """FaceGearLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_LOAD_CASE

    def __init__(self, instance_to_wrap: 'FaceGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2484.FaceGear':
        """FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
