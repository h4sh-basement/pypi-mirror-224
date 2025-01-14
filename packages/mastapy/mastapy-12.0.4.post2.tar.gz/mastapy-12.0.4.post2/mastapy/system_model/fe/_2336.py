﻿"""_2336.py

FEEntityGroupWithSelection
"""


from typing import Generic, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FE_ENTITY_GROUP_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE', 'FEEntityGroupWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('FEEntityGroupWithSelection',)


TGroup = TypeVar('TGroup')
TGroupContents = TypeVar('TGroupContents')


class FEEntityGroupWithSelection(_0.APIBase, Generic[TGroup, TGroupContents]):
    """FEEntityGroupWithSelection

    This is a mastapy class.

    Generic Types:
        TGroup
        TGroupContents
    """

    TYPE = _FE_ENTITY_GROUP_WITH_SELECTION

    def __init__(self, instance_to_wrap: 'FEEntityGroupWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def group(self) -> 'TGroup':
        """TGroup: 'Group' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Group

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_selection_to_group(self):
        """ 'AddSelectionToGroup' is the original name of this method."""

        self.wrapped.AddSelectionToGroup()

    def delete_group(self):
        """ 'DeleteGroup' is the original name of this method."""

        self.wrapped.DeleteGroup()

    def select_items(self):
        """ 'SelectItems' is the original name of this method."""

        self.wrapped.SelectItems()
