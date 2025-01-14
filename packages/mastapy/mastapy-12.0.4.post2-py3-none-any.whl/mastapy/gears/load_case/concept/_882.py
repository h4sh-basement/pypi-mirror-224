﻿"""_882.py

ConceptGearSetLoadCase
"""


from mastapy.gears.load_case import _867
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.Gears.LoadCase.Concept', 'ConceptGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetLoadCase',)


class ConceptGearSetLoadCase(_867.GearSetLoadCaseBase):
    """ConceptGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_LOAD_CASE

    def __init__(self, instance_to_wrap: 'ConceptGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
