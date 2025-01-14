﻿"""_116.py

StiffnessSolver
"""


from mastapy.nodal_analysis.system_solvers import _114
from mastapy._internal.python_net import python_net_import

_STIFFNESS_SOLVER = python_net_import('SMT.MastaAPI.NodalAnalysis.SystemSolvers', 'StiffnessSolver')


__docformat__ = 'restructuredtext en'
__all__ = ('StiffnessSolver',)


class StiffnessSolver(_114.Solver):
    """StiffnessSolver

    This is a mastapy class.
    """

    TYPE = _STIFFNESS_SOLVER

    def __init__(self, instance_to_wrap: 'StiffnessSolver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
