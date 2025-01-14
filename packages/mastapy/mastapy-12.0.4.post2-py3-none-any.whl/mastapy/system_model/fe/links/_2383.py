﻿"""_2383.py

MultiNodeFELink
"""


from mastapy.system_model.fe.links import _2376
from mastapy._internal.python_net import python_net_import

_MULTI_NODE_FE_LINK = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'MultiNodeFELink')


__docformat__ = 'restructuredtext en'
__all__ = ('MultiNodeFELink',)


class MultiNodeFELink(_2376.FELink):
    """MultiNodeFELink

    This is a mastapy class.
    """

    TYPE = _MULTI_NODE_FE_LINK

    def __init__(self, instance_to_wrap: 'MultiNodeFELink.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
