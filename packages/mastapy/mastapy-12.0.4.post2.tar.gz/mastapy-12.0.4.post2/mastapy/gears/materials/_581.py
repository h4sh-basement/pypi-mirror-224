﻿"""_581.py

BevelGearMaterialDatabase
"""


from mastapy.gears.materials import _588, _580
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'BevelGearMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearMaterialDatabase',)


class BevelGearMaterialDatabase(_588.GearMaterialDatabase['_580.BevelGearMaterial']):
    """BevelGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MATERIAL_DATABASE

    def __init__(self, instance_to_wrap: 'BevelGearMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
