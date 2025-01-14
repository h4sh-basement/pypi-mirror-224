﻿"""_1959.py

LoadedAxialThrustNeedleRollerBearingElement
"""


from mastapy.bearings.bearing_results.rolling import _1956
from mastapy._internal.python_net import python_net_import

_LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAxialThrustNeedleRollerBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAxialThrustNeedleRollerBearingElement',)


class LoadedAxialThrustNeedleRollerBearingElement(_1956.LoadedAxialThrustCylindricalRollerBearingElement):
    """LoadedAxialThrustNeedleRollerBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_AXIAL_THRUST_NEEDLE_ROLLER_BEARING_ELEMENT

    def __init__(self, instance_to_wrap: 'LoadedAxialThrustNeedleRollerBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
