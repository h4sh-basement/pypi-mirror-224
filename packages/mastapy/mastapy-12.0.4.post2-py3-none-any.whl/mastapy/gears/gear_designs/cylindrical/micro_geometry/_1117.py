﻿"""_1117.py

ProfileFormReliefWithDeviation
"""


from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1118
from mastapy._internal.python_net import python_net_import

_PROFILE_FORM_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'ProfileFormReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('ProfileFormReliefWithDeviation',)


class ProfileFormReliefWithDeviation(_1118.ProfileReliefWithDeviation):
    """ProfileFormReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _PROFILE_FORM_RELIEF_WITH_DEVIATION

    def __init__(self, instance_to_wrap: 'ProfileFormReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
