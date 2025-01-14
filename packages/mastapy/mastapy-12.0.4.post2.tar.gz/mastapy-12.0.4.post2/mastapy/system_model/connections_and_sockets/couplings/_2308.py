﻿"""_2308.py

PartToPartShearCouplingSocket
"""


from mastapy.system_model.connections_and_sockets.couplings import _2306
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'PartToPartShearCouplingSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingSocket',)


class PartToPartShearCouplingSocket(_2306.CouplingSocket):
    """PartToPartShearCouplingSocket

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_SOCKET

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
