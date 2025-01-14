﻿"""_611.py

CylindricalManufacturedGearMeshDutyCycle
"""


from mastapy.gears.analysis import _1214
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_MESH_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalManufacturedGearMeshDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalManufacturedGearMeshDutyCycle',)


class CylindricalManufacturedGearMeshDutyCycle(_1214.GearMeshImplementationAnalysisDutyCycle):
    """CylindricalManufacturedGearMeshDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_MESH_DUTY_CYCLE

    def __init__(self, instance_to_wrap: 'CylindricalManufacturedGearMeshDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
