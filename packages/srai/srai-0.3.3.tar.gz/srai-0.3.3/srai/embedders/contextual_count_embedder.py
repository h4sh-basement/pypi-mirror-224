"""
Contextual Count Embedder.

This module contains contextual count embedder implementation from ARIC@SIGSPATIAL 2021 paper [1].

References:
    1. https://doi.org/10.1145/3486626.3493434
    1. https://arxiv.org/abs/2111.00990
"""

from typing import List, Optional

import geopandas as gpd
import numpy as np
import pandas as pd
from tqdm import tqdm

from srai.embedders.count_embedder import CountEmbedder
from srai.neighbourhoods import Neighbourhood
from srai.neighbourhoods._base import IndexType


class ContextualCountEmbedder(CountEmbedder):
    """ContextualCountEmbedder."""

    def __init__(
        self,
        neighbourhood: Neighbourhood[IndexType],
        neighbourhood_distance: int,
        concatenate_vectors: bool = False,
        expected_output_features: Optional[List[str]] = None,
        count_subcategories: bool = False,
    ) -> None:
        """
        Init ContextualCountEmbedder.

        Args:
            neighbourhood (Neighbourhood[T]): Neighbourhood object used to get neighbours for
                the contextualization.
            neighbourhood_distance (int): How many neighbours levels should be included in
                the embedding.
            concatenate_vectors (bool, optional): Whether to sum all neighbours into a single vector
                with the same width as `CountEmbedder`, or to concatenate them to the wide format
                and keep all neighbour levels separate. Defaults to False.
            expected_output_features (List[str], optional): The features that are expected
                to be found in the resulting embedding. If not None, the missing features are
                added and filled with 0. The unexpected features are removed.
                The resulting columns are sorted accordingly. Defaults to None.
            count_subcategories (bool, optional): Whether to count all subcategories individually
                or count features only on the highest level based on features column name.
                Defaults to False.

        Raises:
            ValueError: If `neighbourhood_distance` is negative.
        """
        super().__init__(expected_output_features, count_subcategories)

        self.neighbourhood = neighbourhood
        self.neighbourhood_distance = neighbourhood_distance
        self.concatenate_vectors = concatenate_vectors

        if self.neighbourhood_distance < 0:
            raise ValueError("Neighbourhood distance must be positive.")

    def transform(
        self,
        regions_gdf: gpd.GeoDataFrame,
        features_gdf: gpd.GeoDataFrame,
        joint_gdf: gpd.GeoDataFrame,
    ) -> pd.DataFrame:
        """
        Embed a given GeoDataFrame.

        Creates region embeddings by counting the frequencies of each feature value and applying
        a contextualization based on neighbours of regions. For each region, features will be
        altered based on the neighbours either by adding averaged values dimished based on distance,
        or by adding new separate columns with neighbour distance postfix.
        Expects features_gdf to be in wide format with each column being a separate type of
        feature (e.g. amenity, leisure) and rows to hold values of these features for each object.
        The rows will hold numbers of this type of feature in each region. Numbers can be
        fractional because neighbourhoods are averaged to represent a single value from
        all neighbours on a given level.

        Args:
            regions_gdf (gpd.GeoDataFrame): Region indexes and geometries.
            features_gdf (gpd.GeoDataFrame): Feature indexes, geometries and feature values.
            joint_gdf (gpd.GeoDataFrame): Joiner result with region-feature multi-index.

        Returns:
            pd.DataFrame: Embedding for each region in regions_gdf.

        Raises:
            ValueError: If features_gdf is empty and self.expected_output_features is not set.
            ValueError: If any of the gdfs index names is None.
            ValueError: If joint_gdf.index is not of type pd.MultiIndex or doesn't have 2 levels.
            ValueError: If index levels in gdfs don't overlap correctly.
        """
        counts_df = super().transform(regions_gdf, features_gdf, joint_gdf)

        result_df: pd.DataFrame
        if self.concatenate_vectors:
            result_df = self._get_concatenated_embeddings(counts_df)
        else:
            result_df = self._get_squashed_embeddings(counts_df)

        return result_df

    def _get_squashed_embeddings(self, counts_df: pd.DataFrame) -> pd.DataFrame:
        """
        Generate embeddings for regions by summing all neighbourhood levels.

        Creates embedding by getting an average of a neighbourhood at a given distance and adding it
        to the base values with weight equal to 1 / (distance + 1) squared. This way, farther
        neighbourhoods have lower impact on feature values.

        Args:
            counts_df (pd.DataFrame): Calculated features from CountEmbedder.

        Returns:
            pd.DataFrame: Embedding for each region in regions_gdf with number of features equal to
                the same as returned by the CountEmbedder.
        """
        base_columns = list(counts_df.columns)

        result_array = counts_df.values.astype(float)
        for idx, region_id in tqdm(
            enumerate(counts_df.index), desc="Generating embeddings", total=len(counts_df.index)
        ):
            if self.neighbourhood_distance == 0:
                continue

            for distance in range(1, self.neighbourhood_distance + 1):
                neighbours = self.neighbourhood.get_neighbours_at_distance(region_id, distance)
                matching_neighbours = counts_df.index.intersection(neighbours)
                if matching_neighbours.empty:
                    continue

                values = counts_df.loc[matching_neighbours].values
                flattened_values = np.average(values, axis=0)
                result_array[idx, :] += flattened_values / ((distance + 1) ** 2)

        return pd.DataFrame(data=result_array, index=counts_df.index, columns=base_columns)

    def _get_concatenated_embeddings(self, counts_df: pd.DataFrame) -> pd.DataFrame:
        """
        Generate embeddings for regions by concatenating different neighbourhood levels.

        Creates embedding by getting an average of a neighbourhood at a given distance and adding
        those features as separate columns with a postfix added to feature name. This way,
        all neighbourhoods can be analyzed separately, but number of columns grows linearly with
        a distance.

        Args:
            counts_df (pd.DataFrame): Calculated features from CountEmbedder.

        Returns:
            pd.DataFrame: Embedding for each region in regions_gdf with number of features equal to
                a number of features returned by the CountEmbedder multiplied
                by (neighbourhood distance + 1).
        """
        base_columns = list(counts_df.columns)
        no_base_columns = len(base_columns)
        columns = [
            f"{column}_{distance}"
            for distance in range(self.neighbourhood_distance + 1)
            for column in base_columns
        ]

        result_array = np.zeros(shape=(len(counts_df.index), len(columns)))
        result_array[:, 0:no_base_columns] = counts_df.values
        for idx, region_id in tqdm(
            enumerate(counts_df.index), desc="Generating embeddings", total=len(counts_df.index)
        ):
            if self.neighbourhood_distance == 0:
                continue

            for distance in range(1, self.neighbourhood_distance + 1):
                neighbours = self.neighbourhood.get_neighbours_at_distance(region_id, distance)
                matching_neighbours = counts_df.index.intersection(neighbours)
                if matching_neighbours.empty:
                    continue

                values = counts_df.loc[matching_neighbours].values
                flattened_values = np.average(values, axis=0)
                result_array[idx, no_base_columns * distance : no_base_columns * (distance + 1)] = (
                    flattened_values
                )

        return pd.DataFrame(data=result_array, index=counts_df.index, columns=columns)
