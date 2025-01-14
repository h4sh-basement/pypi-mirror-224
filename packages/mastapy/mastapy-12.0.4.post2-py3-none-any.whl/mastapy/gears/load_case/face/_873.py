﻿"""_873.py

FaceGearSetLoadCase
"""


from mastapy.gears.load_case import _867
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Face', 'FaceGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetLoadCase',)


class FaceGearSetLoadCase(_867.GearSetLoadCaseBase):
    """FaceGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_LOAD_CASE

    def __init__(self, instance_to_wrap: 'FaceGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
