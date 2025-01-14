﻿"""_1463.py

ComplexVector3D
"""


from mastapy.math_utility import _1462
from mastapy._internal.python_net import python_net_import

_COMPLEX_VECTOR_3D = python_net_import('SMT.MastaAPI.MathUtility', 'ComplexVector3D')


__docformat__ = 'restructuredtext en'
__all__ = ('ComplexVector3D',)


class ComplexVector3D(_1462.ComplexVector):
    """ComplexVector3D

    This is a mastapy class.
    """

    TYPE = _COMPLEX_VECTOR_3D

    def __init__(self, instance_to_wrap: 'ComplexVector3D.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
