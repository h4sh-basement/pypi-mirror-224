﻿"""_95.py

MomentInputComponent
"""


from mastapy._internal import constructor
from mastapy.nodal_analysis.varying_input_components import _92
from mastapy._internal.python_net import python_net_import

_MOMENT_INPUT_COMPONENT = python_net_import('SMT.MastaAPI.NodalAnalysis.VaryingInputComponents', 'MomentInputComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('MomentInputComponent',)


class MomentInputComponent(_92.AbstractVaryingInputComponent):
    """MomentInputComponent

    This is a mastapy class.
    """

    TYPE = _MOMENT_INPUT_COMPONENT

    def __init__(self, instance_to_wrap: 'MomentInputComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def moment(self) -> 'float':
        """float: 'Moment' is the original name of this property."""

        temp = self.wrapped.Moment

        if temp is None:
            return 0.0

        return temp

    @moment.setter
    def moment(self, value: 'float'):
        self.wrapped.Moment = float(value) if value is not None else 0.0
