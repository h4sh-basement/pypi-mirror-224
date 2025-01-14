﻿"""_2285.py

StraightBevelDiffGearTeethSocket
"""


from mastapy.system_model.connections_and_sockets.gears import _2263
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_TEETH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'StraightBevelDiffGearTeethSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearTeethSocket',)


class StraightBevelDiffGearTeethSocket(_2263.BevelGearTeethSocket):
    """StraightBevelDiffGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_TEETH_SOCKET

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearTeethSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
