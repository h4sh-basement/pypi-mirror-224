﻿"""_379.py

KlingelnbergSpiralBevelVirtualCylindricalGear
"""


from mastapy.gears.rating.virtual_cylindrical_gears import _380
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_SPIRAL_BEVEL_VIRTUAL_CYLINDRICAL_GEAR = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'KlingelnbergSpiralBevelVirtualCylindricalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergSpiralBevelVirtualCylindricalGear',)


class KlingelnbergSpiralBevelVirtualCylindricalGear(_380.KlingelnbergVirtualCylindricalGear):
    """KlingelnbergSpiralBevelVirtualCylindricalGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_SPIRAL_BEVEL_VIRTUAL_CYLINDRICAL_GEAR

    def __init__(self, instance_to_wrap: 'KlingelnbergSpiralBevelVirtualCylindricalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
