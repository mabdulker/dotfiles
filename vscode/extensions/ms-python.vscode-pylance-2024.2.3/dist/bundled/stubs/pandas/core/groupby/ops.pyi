from collections.abc import Sequence

import numpy as np
from pandas import (
    DataFrame,
    Index,
    Series,
)
from pandas.core.groupby import grouper

class BaseGrouper:
    axis = ...
    sort = ...
    group_keys = ...
    mutated = ...
    indexer = ...
    def __init__(
        self,
        axis: Index,
        groupings: Sequence[grouper.Grouping],
        sort: bool = ...,
        group_keys: bool = ...,
        mutated: bool = ...,
        indexer: np.ndarray | None = ...,
    ) -> None: ...
    @property
    def groupings(self) -> list[grouper.Grouping]: ...
    @property
    def shape(self): ...
    def __iter__(self): ...
    @property
    def nkeys(self) -> int: ...
    def get_iterator(self, data: DataFrame | Series, axis: int = ...): ...
    def apply(self, f, data: DataFrame | Series, axis: int = ...): ...
    def indices(self): ...
    @property
    def codes(self) -> list[np.ndarray]: ...
    @property
    def levels(self) -> list[Index]: ...
    @property
    def names(self): ...
    def size(self) -> Series: ...
    def groups(self): ...
    def is_monotonic(self) -> bool: ...
    def group_info(self): ...
    def codes_info(self) -> np.ndarray: ...
    def ngroups(self) -> int: ...
    @property
    def reconstructed_codes(self) -> list[np.ndarray]: ...
    def result_index(self) -> Index: ...
    def get_group_levels(self): ...
    def agg_series(self, obj: Series, func): ...

class BinGrouper(BaseGrouper):
    bins = ...
    binlabels = ...
    mutated = ...
    indexer = ...
    def __init__(
        self,
        bins,
        binlabels,
        filter_empty: bool = ...,
        mutated: bool = ...,
        indexer=...,
    ) -> None: ...
    def groups(self): ...
    @property
    def nkeys(self) -> int: ...
    def get_iterator(self, data: DataFrame | Series, axis: int = ...): ...
    def indices(self): ...
    def group_info(self): ...
    @property
    def reconstructed_codes(self) -> list[np.ndarray]: ...
    def result_index(self): ...
    @property
    def levels(self): ...
    @property
    def names(self): ...
    @property
    def groupings(self) -> list[grouper.Grouping]: ...
    def agg_series(self, obj: Series, func): ...

class DataSplitter:
    data = ...
    labels = ...
    ngroups = ...
    axis = ...
    def __init__(
        self, data: DataFrame | Series, labels, ngroups: int, axis: int = ...
    ) -> None: ...
    def slabels(self): ...
    def __iter__(self): ...

class SeriesSplitter(DataSplitter): ...
class FrameSplitter(DataSplitter): ...

def get_splitter(data: DataFrame | Series, *args, **kwargs) -> DataSplitter: ...
