﻿"""_841.py

GearStiffnessNode
"""


from mastapy.nodal_analysis import _67
from mastapy._internal.python_net import python_net_import

_GEAR_STIFFNESS_NODE = python_net_import('SMT.MastaAPI.Gears.LTCA', 'GearStiffnessNode')


__docformat__ = 'restructuredtext en'
__all__ = ('GearStiffnessNode',)


class GearStiffnessNode(_67.FEStiffnessNode):
    """GearStiffnessNode

    This is a mastapy class.
    """

    TYPE = _GEAR_STIFFNESS_NODE

    def __init__(self, instance_to_wrap: 'GearStiffnessNode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
