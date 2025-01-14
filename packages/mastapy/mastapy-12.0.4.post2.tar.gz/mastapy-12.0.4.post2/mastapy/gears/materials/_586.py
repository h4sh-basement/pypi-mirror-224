﻿"""_586.py

CylindricalGearPlasticMaterialDatabase
"""


from mastapy.gears.materials import _585, _596
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLASTIC_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.Gears.Materials', 'CylindricalGearPlasticMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPlasticMaterialDatabase',)


class CylindricalGearPlasticMaterialDatabase(_585.CylindricalGearMaterialDatabase['_596.PlasticCylindricalGearMaterial']):
    """CylindricalGearPlasticMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PLASTIC_MATERIAL_DATABASE

    def __init__(self, instance_to_wrap: 'CylindricalGearPlasticMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
