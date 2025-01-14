"""Utility H3 related functions."""

from sys import platform
from typing import Iterable, List, Literal, Tuple, Union, overload

import geopandas as gpd
import h3
import numpy as np
import numpy.typing as npt
from h3ronpy.arrow.vector import cells_to_wkb_polygons, wkb_to_cells
from shapely.geometry import Point, Polygon
from shapely.geometry.base import BaseGeometry

from srai.constants import GEOMETRY_COLUMN, WGS84_CRS
from srai.geometry import buffer_geometry

__all__ = [
    "shapely_geometry_to_h3",
    "h3_to_geoseries",
    "h3_to_shapely_geometry",
    "get_local_ij_index",
]


def shapely_geometry_to_h3(
    geometry: Union[BaseGeometry, Iterable[BaseGeometry], gpd.GeoSeries, gpd.GeoDataFrame],
    h3_resolution: int,
    buffer: bool = True,
) -> List[str]:
    """
    Convert Shapely geometry to H3 indexes.

    Args:
        geometry (Union[BaseGeometry, Iterable[BaseGeometry], GeoSeries, GeoDataFrame]):
            Shapely geometry to be converted.
        h3_resolution (int): H3 resolution of the cells. See [1] for a full comparison.
        buffer (bool, optional): Whether to fully cover the geometries with
            H3 Cells (visible on the borders). Defaults to True.

    Returns:
        List[str]: List of H3 indexes that cover a given geometry.

    Raises:
        ValueError: If resolution is not between 0 and 15.

    References:
        1. https://h3geo.org/docs/core-library/restable/
    """
    if not (0 <= h3_resolution <= 15):
        raise ValueError(f"Resolution {h3_resolution} is not between 0 and 15.")

    if _is_macos():
        return _polygon_to_h3_index_raw(geometry, h3_resolution, buffer)

    wkb = []
    if isinstance(geometry, gpd.GeoSeries):
        wkb = geometry.to_wkb()
    elif isinstance(geometry, gpd.GeoDataFrame):
        wkb = geometry[GEOMETRY_COLUMN].to_wkb()
    elif isinstance(geometry, Iterable):
        wkb = [sub_geometry.wkb for sub_geometry in geometry]
    else:
        wkb = [geometry.wkb]

    h3_indexes = wkb_to_cells(
        wkb, resolution=h3_resolution, all_intersecting=buffer, flatten=True
    ).unique()

    return [h3.int_to_str(h3_index) for h3_index in h3_indexes.tolist()]


def _polygon_to_h3_index_raw(
    geometry: Union[BaseGeometry, Iterable[BaseGeometry], gpd.GeoSeries, gpd.GeoDataFrame],
    h3_resolution: int,
    buffer: bool = True,
) -> List[str]:
    def _polygon_shapely_to_h3(
        geometry: Union[Point, Polygon], h3_resolution: int, buffer: bool
    ) -> List[str]:
        if isinstance(geometry, Point):
            return [h3.latlng_to_cell(geometry.y, geometry.x, h3_resolution)]

        buffer_distance_meters = 2 * h3.average_hexagon_edge_length(h3_resolution, unit="m")

        buffered_geometry = (
            buffer_geometry(geometry, buffer_distance_meters) if buffer else geometry
        )

        exterior = [coord[::-1] for coord in list(buffered_geometry.exterior.coords)]
        interiors = [
            [coord[::-1] for coord in list(interior.coords)]
            for interior in buffered_geometry.interiors
        ]
        h3_cells: List[str] = h3.polygon_to_cells(h3.Polygon(exterior, *interiors), h3_resolution)

        if buffer:
            h3_cells = [
                h3_cell
                for h3_cell in h3_cells
                if _h3_index_to_polygon_raw(h3_cell).intersects(geometry)
            ]

        return h3_cells

    from functional import seq

    geoseries: gpd.GeoSeries

    if isinstance(geometry, gpd.GeoSeries):
        geoseries = geometry
    elif isinstance(geometry, gpd.GeoDataFrame):
        geoseries = geometry[GEOMETRY_COLUMN]
    elif isinstance(geometry, Iterable):
        geoseries = gpd.GeoSeries(geometry, crs=WGS84_CRS)
    else:
        return _polygon_to_h3_index_raw([geometry], h3_resolution, buffer)

    geoseries = geoseries.explode(ignore_index=True, index_parts=True)

    h3_indexes: List[str] = (
        seq(geoseries)
        .flat_map(lambda polygon: _polygon_shapely_to_h3(polygon, h3_resolution, buffer))
        .distinct()
        .to_list()
    )

    return h3_indexes


# TODO: write tests (#322)
def h3_to_geoseries(h3_index: Union[int, str, Iterable[Union[int, str]]]) -> gpd.GeoSeries:
    """
    Convert H3 index to GeoPandas GeoSeries.

    Args:
        h3_index (Union[int, str, Iterable[Union[int, str]]]): H3 index (or list of indexes)
            to be converted.

    Returns:
        GeoSeries: Geometries as GeoSeries with default CRS applied.
    """
    if isinstance(h3_index, (str, int)):
        return h3_to_geoseries([h3_index])
    else:
        if _is_macos():
            return gpd.GeoSeries(
                [_h3_index_to_polygon_raw(h3_cell) for h3_cell in h3_index], crs=WGS84_CRS
            )

        h3_int_indexes = (
            h3_cell if isinstance(h3_cell, int) else h3.str_to_int(h3_cell) for h3_cell in h3_index
        )
        return gpd.GeoSeries.from_wkb(cells_to_wkb_polygons(h3_int_indexes), crs=WGS84_CRS)


def _h3_index_to_polygon_raw(h3_index: Union[int, str]) -> Polygon:
    if isinstance(h3_index, int):
        h3_index = h3.int_to_str(h3_index)
    h3_poly = h3.cells_to_polygons([h3_index])[0]

    return Polygon(
        shell=[coord[::-1] for coord in h3_poly.outer],
        holes=[[coord[::-1] for coord in hole] for hole in h3_poly.holes],
    )


@overload
def h3_to_shapely_geometry(h3_index: Union[int, str]) -> Polygon:
    ...


@overload
def h3_to_shapely_geometry(h3_index: Iterable[Union[int, str]]) -> List[Polygon]:
    ...


# TODO: write tests (#322)
def h3_to_shapely_geometry(
    h3_index: Union[int, str, Iterable[Union[int, str]]]
) -> Union[Polygon, List[Polygon]]:
    """
    Convert H3 index to Shapely polygon.

    Args:
        h3_index (Union[int, str, Iterable[Union[int, str]]]): H3 index (or list of indexes)
            to be converted.

    Returns:
        Union[Polygon, List[Polygon]]: Converted polygon (or list of polygons).
    """
    if isinstance(h3_index, (str, int)):
        coords = h3.cell_to_boundary(h3_index, geo_json=True)
        return Polygon(coords)
    return h3_to_geoseries(h3_index).values.tolist()


@overload
def get_local_ij_index(origin_index: str, h3_index: str) -> Tuple[int, int]:
    ...


@overload
def get_local_ij_index(
    origin_index: str, h3_index: List[str], return_as_numpy: Literal[False]
) -> List[Tuple[int, int]]:
    ...


@overload
def get_local_ij_index(
    origin_index: str, h3_index: List[str], return_as_numpy: Literal[True]
) -> npt.NDArray[np.int8]:
    ...


# Last fallback needed as per documentation:
# https://mypy.readthedocs.io/en/stable/literal_types.html#literal-types
@overload
def get_local_ij_index(
    origin_index: str, h3_index: List[str], return_as_numpy: bool
) -> Union[List[Tuple[int, int]], npt.NDArray[np.int8]]:
    ...


def get_local_ij_index(
    origin_index: str, h3_index: Union[str, List[str]], return_as_numpy: bool = False
) -> Union[Tuple[int, int], List[Tuple[int, int]], npt.NDArray[np.int8]]:
    """
    Calculate the local H3 ij index based on provided origin index.

    Wraps H3's cell_to_local_ij function and centers returned coordinates
    around provided origin cell.

    Args:
        origin_index (str): H3 index of the origin region.
        h3_index (Union[str, List[str]]): H3 index of the second region or list of regions.
        return_as_numpy (bool, optional): Flag whether to return calculated indexes as a Numpy array
            or a list of tuples.

    Returns:
        Union[Tuple[int, int], List[Tuple[int, int]], npt.NDArray[np.int8]]: The local ij index of
            the second region (or regions) with respect to the first one.
    """
    origin_coords = h3.cell_to_local_ij(origin_index, origin_index)
    if isinstance(h3_index, str):
        ijs = h3.cell_to_local_ij(origin_index, h3_index)
        return (origin_coords[0] - ijs[0], origin_coords[1] - ijs[1])
    ijs = np.array([h3.cell_to_local_ij(origin_index, h3_cell) for h3_cell in h3_index])
    local_ijs = np.array(origin_coords) - ijs

    if not return_as_numpy:
        local_ijs = [(coords[0], coords[1]) for coords in local_ijs]

    return local_ijs


def _is_macos() -> bool:
    """Return flag if code is run on OS X."""
    return platform == "darwin"
