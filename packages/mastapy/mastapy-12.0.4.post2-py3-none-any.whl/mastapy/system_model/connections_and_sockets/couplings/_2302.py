﻿"""_2302.py

ClutchSocket
"""


from mastapy.system_model.connections_and_sockets.couplings import _2306
from mastapy._internal.python_net import python_net_import

_CLUTCH_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'ClutchSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchSocket',)


class ClutchSocket(_2306.CouplingSocket):
    """ClutchSocket

    This is a mastapy class.
    """

    TYPE = _CLUTCH_SOCKET

    def __init__(self, instance_to_wrap: 'ClutchSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
