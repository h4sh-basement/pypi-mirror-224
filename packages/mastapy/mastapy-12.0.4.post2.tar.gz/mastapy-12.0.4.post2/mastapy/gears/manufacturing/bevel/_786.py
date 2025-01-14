﻿"""_786.py

ConicalSetMicroGeometryConfigBase
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _319
from mastapy.gears.analysis import _1221
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MICRO_GEOMETRY_CONFIG_BASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalSetMicroGeometryConfigBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalSetMicroGeometryConfigBase',)


class ConicalSetMicroGeometryConfigBase(_1221.GearSetImplementationDetail):
    """ConicalSetMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MICRO_GEOMETRY_CONFIG_BASE

    def __init__(self, instance_to_wrap: 'ConicalSetMicroGeometryConfigBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compound_layer_thickness(self) -> 'float':
        """float: 'CompoundLayerThickness' is the original name of this property."""

        temp = self.wrapped.CompoundLayerThickness

        if temp is None:
            return 0.0

        return temp

    @compound_layer_thickness.setter
    def compound_layer_thickness(self, value: 'float'):
        self.wrapped.CompoundLayerThickness = float(value) if value is not None else 0.0

    @property
    def deflection_from_bending_option(self) -> '_319.DeflectionFromBendingOption':
        """DeflectionFromBendingOption: 'DeflectionFromBendingOption' is the original name of this property."""

        temp = self.wrapped.DeflectionFromBendingOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_319.DeflectionFromBendingOption)(value) if value is not None else None

    @deflection_from_bending_option.setter
    def deflection_from_bending_option(self, value: '_319.DeflectionFromBendingOption'):
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DeflectionFromBendingOption = value

    @property
    def file_location_for_contact_chart(self) -> 'str':
        """str: 'FileLocationForContactChart' is the original name of this property."""

        temp = self.wrapped.FileLocationForContactChart

        if temp is None:
            return ''

        return temp

    @file_location_for_contact_chart.setter
    def file_location_for_contact_chart(self, value: 'str'):
        self.wrapped.FileLocationForContactChart = str(value) if value is not None else ''

    @property
    def number_of_columns_for_grid(self) -> 'int':
        """int: 'NumberOfColumnsForGrid' is the original name of this property."""

        temp = self.wrapped.NumberOfColumnsForGrid

        if temp is None:
            return 0

        return temp

    @number_of_columns_for_grid.setter
    def number_of_columns_for_grid(self, value: 'int'):
        self.wrapped.NumberOfColumnsForGrid = int(value) if value is not None else 0

    @property
    def number_of_points_for_interpolated_surface_u(self) -> 'int':
        """int: 'NumberOfPointsForInterpolatedSurfaceU' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForInterpolatedSurfaceU

        if temp is None:
            return 0

        return temp

    @number_of_points_for_interpolated_surface_u.setter
    def number_of_points_for_interpolated_surface_u(self, value: 'int'):
        self.wrapped.NumberOfPointsForInterpolatedSurfaceU = int(value) if value is not None else 0

    @property
    def number_of_points_for_interpolated_surface_v(self) -> 'int':
        """int: 'NumberOfPointsForInterpolatedSurfaceV' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForInterpolatedSurfaceV

        if temp is None:
            return 0

        return temp

    @number_of_points_for_interpolated_surface_v.setter
    def number_of_points_for_interpolated_surface_v(self, value: 'int'):
        self.wrapped.NumberOfPointsForInterpolatedSurfaceV = int(value) if value is not None else 0

    @property
    def number_of_rows_for_fillet_grid(self) -> 'int':
        """int: 'NumberOfRowsForFilletGrid' is the original name of this property."""

        temp = self.wrapped.NumberOfRowsForFilletGrid

        if temp is None:
            return 0

        return temp

    @number_of_rows_for_fillet_grid.setter
    def number_of_rows_for_fillet_grid(self, value: 'int'):
        self.wrapped.NumberOfRowsForFilletGrid = int(value) if value is not None else 0

    @property
    def number_of_rows_for_flank_grid(self) -> 'int':
        """int: 'NumberOfRowsForFlankGrid' is the original name of this property."""

        temp = self.wrapped.NumberOfRowsForFlankGrid

        if temp is None:
            return 0

        return temp

    @number_of_rows_for_flank_grid.setter
    def number_of_rows_for_flank_grid(self, value: 'int'):
        self.wrapped.NumberOfRowsForFlankGrid = int(value) if value is not None else 0

    @property
    def single_tooth_stiffness(self) -> 'float':
        """float: 'SingleToothStiffness' is the original name of this property."""

        temp = self.wrapped.SingleToothStiffness

        if temp is None:
            return 0.0

        return temp

    @single_tooth_stiffness.setter
    def single_tooth_stiffness(self, value: 'float'):
        self.wrapped.SingleToothStiffness = float(value) if value is not None else 0.0

    @property
    def write_contact_chart_to_file_after_solve(self) -> 'bool':
        """bool: 'WriteContactChartToFileAfterSolve' is the original name of this property."""

        temp = self.wrapped.WriteContactChartToFileAfterSolve

        if temp is None:
            return False

        return temp

    @write_contact_chart_to_file_after_solve.setter
    def write_contact_chart_to_file_after_solve(self, value: 'bool'):
        self.wrapped.WriteContactChartToFileAfterSolve = bool(value) if value is not None else False
