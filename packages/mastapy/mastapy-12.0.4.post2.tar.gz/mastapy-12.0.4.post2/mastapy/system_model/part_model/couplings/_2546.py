﻿"""_2546.py

Pulley
"""


from mastapy.system_model.part_model.couplings import _2540
from mastapy._internal.python_net import python_net_import

_PULLEY = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Pulley')


__docformat__ = 'restructuredtext en'
__all__ = ('Pulley',)


class Pulley(_2540.CouplingHalf):
    """Pulley

    This is a mastapy class.
    """

    TYPE = _PULLEY

    def __init__(self, instance_to_wrap: 'Pulley.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
