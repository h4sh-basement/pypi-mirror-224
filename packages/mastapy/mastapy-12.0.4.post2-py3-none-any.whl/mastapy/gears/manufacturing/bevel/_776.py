﻿"""_776.py

ConicalMeshFlankNurbsMicroGeometryConfig
"""


from mastapy.gears.manufacturing.bevel import _775
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FLANK_NURBS_MICRO_GEOMETRY_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshFlankNurbsMicroGeometryConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshFlankNurbsMicroGeometryConfig',)


class ConicalMeshFlankNurbsMicroGeometryConfig(_775.ConicalMeshFlankMicroGeometryConfig):
    """ConicalMeshFlankNurbsMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FLANK_NURBS_MICRO_GEOMETRY_CONFIG

    def __init__(self, instance_to_wrap: 'ConicalMeshFlankNurbsMicroGeometryConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
