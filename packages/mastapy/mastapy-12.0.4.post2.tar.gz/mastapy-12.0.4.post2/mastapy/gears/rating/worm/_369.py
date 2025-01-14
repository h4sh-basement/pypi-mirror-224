﻿"""_369.py

WormGearSetDutyCycleRating
"""


from mastapy.gears.rating import _356
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Worm', 'WormGearSetDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetDutyCycleRating',)


class WormGearSetDutyCycleRating(_356.GearSetDutyCycleRating):
    """WormGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_DUTY_CYCLE_RATING

    def __init__(self, instance_to_wrap: 'WormGearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
