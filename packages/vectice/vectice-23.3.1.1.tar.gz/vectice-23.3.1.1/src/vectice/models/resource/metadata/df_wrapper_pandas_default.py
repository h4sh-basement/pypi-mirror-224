from __future__ import annotations

import logging
from abc import abstractmethod
from typing import Generic, TypeVar

from pandas import Series, api

from vectice.models.resource.metadata.column_metadata import (
    BooleanStat,
    Column,
    ColumnCategoryType,
    DateStat,
    MostCommon,
    NumericalStat,
    Quantiles,
    Size,
    TextStat,
)
from vectice.models.resource.metadata.dataframe_config import (
    MAX_COLUMNS_CAPTURE_STATS,
    DataFramePandasType,
)
from vectice.models.resource.metadata.df_wrapper_resource import DataFrameWrapper

_logger = logging.getLogger(__name__)

PT = TypeVar("PT", bound=DataFramePandasType)


class DataFrameDefaultPandasWrapper(DataFrameWrapper[PT], Generic[PT]):
    rows: int
    columns_numbers: int

    def __init__(self, dataframe: PT):
        super().__init__(dataframe)
        self.rows, self.columns_numbers = self.dataframe.shape

    @abstractmethod
    def __compute_date_column_statistics__(self, series: Series) -> DateStat:
        pass

    def get_size(self) -> Size:
        return Size(rows=int(self.rows), columns=int(self.columns_numbers))

    def is_date_series(self, column_type: str) -> bool:
        if api.types.is_datetime64_any_dtype(column_type):
            return True

        try:
            # Temporary fixing issue -> TypeError: data type 'dbdate' not understood [EN-2534]
            if column_type == "dbdate":
                return True
        except TypeError:
            pass

        return False

    def capture_column_schema(self) -> list[Column]:
        column_cat: ColumnCategoryType | None = None
        list_schema: list[Column] = []

        for column, column_type in self.dataframe.dtypes.items():
            column = str(column)
            if api.types.is_bool_dtype(column_type):
                column_cat = ColumnCategoryType.BOOLEAN
                dtype = str(column_type)
            elif api.types.is_numeric_dtype(column_type):
                column_cat = ColumnCategoryType.NUMERICAL
                dtype = str(column_type)
            elif self.is_date_series(column_type):
                column_cat = ColumnCategoryType.DATE
                dtype = str(column_type)
            elif api.types.is_string_dtype(column_type):
                column_cat = ColumnCategoryType.TEXT
                dtype = str(column_type)
            else:
                column_cat = None
                dtype = str(column_type)

            list_schema.append(
                Column(
                    name=column,
                    data_type=dtype if dtype != "object" else "string",
                    stats=None,
                    category_type=column_cat,
                )
            )
        return list_schema

    def capture_column_statistics(self, list_col_schema: list[Column]) -> list[Column]:
        columns: list[Column] = []
        stat: TextStat | BooleanStat | NumericalStat | DateStat | None = None
        for idx, col in enumerate(list_col_schema):
            if idx == MAX_COLUMNS_CAPTURE_STATS:
                _logger.warning(
                    f"Statistics are only captured for the first {MAX_COLUMNS_CAPTURE_STATS} columns of your dataframe."
                )
            column = self.dataframe[col.name]
            col_type = col.category_type
            if col_type is not None and idx < MAX_COLUMNS_CAPTURE_STATS:
                stat = self.__capture_pandas_stats__(column, col_type)
            else:
                stat = None
            col.stats = stat

            columns.append(col)
        return columns

    def __capture_pandas_stats__(
        self, series: Series, col_type: ColumnCategoryType
    ) -> TextStat | BooleanStat | NumericalStat | DateStat | None:
        if col_type.value == "BOOLEAN":
            return self.__compute_boolean_column_statistics__(series)
        elif col_type.value == "NUMERICAL":
            return self.__compute_numeric_column_statistics__(series)
        elif col_type.value == "DATE":
            return self.__compute_date_column_statistics__(series)
        elif col_type.value == "TEXT":
            return self.__compute_string_column_statistics__(series)
        return None

    def __compute_boolean_column_statistics__(self, series: Series) -> BooleanStat:
        """Parse a dataframe series and return statistics about it.

        The computed statistics are:
        - The percentage of True
        - The percentage of False
        - The count missing value in %
        Parameters:
            series: The pandas series to get information from.

        Returns:
            A BooleanStat object containing the above statistics.
        """
        value_counts = series.value_counts(dropna=False)
        value_counts_percentage = value_counts / value_counts.sum()
        series_missing = series.isnull().sum()
        missing = series_missing / len(series)

        return BooleanStat(
            true=float(value_counts_percentage[True]),
            false=float(value_counts_percentage[False]),
            missing=float(missing),
        )

    def __compute_numeric_column_statistics__(self, series: Series) -> NumericalStat:
        """Parse a dataframe series and return statistics about it.

        The computed statistics are:
        - the mean
        - the standard deviation
        - the min value
        - the 25% percentiles
        - the 50% percentiles
        - the 75% percentiles
        - the max value
        - the count missing value in %
        Parameters:
            series: The pandas series to get information from.

        Returns:
            A NumericalStat object containing the above statistics.
        """
        mean = series.mean()
        std = series.std()
        min_q = series.min()
        q25 = series.quantile(0.25)
        q50 = series.quantile(0.5)
        q75 = series.quantile(0.75)
        max_q = series.max()
        missing = float(series.isnull().sum()) / float(len(series))

        return NumericalStat(
            mean=float(mean),
            std_deviation=float(std),
            quantiles=Quantiles(q_min=float(min_q), q25=float(q25), q50=float(q50), q75=float(q75), q_max=float(max_q)),
            missing=float(missing),
        )

    def __compute_string_column_statistics__(self, series: Series) -> TextStat:
        """Parse a dataframe series and return statistics about it.

        The computed statistics are:
        - the unique number of value
        - the top 3 most common values with their percentages
        - the count missing value in %
        Parameters:
            series: The pandas series to get information from.

        Returns:
            A TextStat object containing the above statistics.
        """
        missing = series.isnull().sum() / len(series)
        unique = len(series.unique())
        value_counts = series.value_counts() / series.value_counts(dropna=False).sum()

        size = 3 if unique >= 3 else unique
        value_counts_largest: Series[float] = value_counts.nlargest(size)

        return TextStat(
            unique=float(unique),
            missing=float(missing),
            most_commons=[
                MostCommon(str(i), float(value_counts_largest[i])) for i in value_counts_largest.index.values
            ],
        )
