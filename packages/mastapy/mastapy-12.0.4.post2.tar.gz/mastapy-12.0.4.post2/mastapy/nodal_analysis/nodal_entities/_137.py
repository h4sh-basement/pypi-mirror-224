﻿"""_137.py

GearMeshNodePair
"""


from mastapy.nodal_analysis.nodal_entities import _124
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_NODE_PAIR = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'GearMeshNodePair')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshNodePair',)


class GearMeshNodePair(_124.ArbitraryNodalComponent):
    """GearMeshNodePair

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_NODE_PAIR

    def __init__(self, instance_to_wrap: 'GearMeshNodePair.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
