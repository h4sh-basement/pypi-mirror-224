﻿"""_844.py

CylindricalGearBendingStiffness
"""


from mastapy.gears.ltca import _826
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_BENDING_STIFFNESS = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearBendingStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearBendingStiffness',)


class CylindricalGearBendingStiffness(_826.GearBendingStiffness):
    """CylindricalGearBendingStiffness

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_BENDING_STIFFNESS

    def __init__(self, instance_to_wrap: 'CylindricalGearBendingStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
