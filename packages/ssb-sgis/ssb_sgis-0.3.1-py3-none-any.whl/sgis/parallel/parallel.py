import functools
import multiprocessing
from pathlib import Path
from typing import Any, Callable, Iterable, Sized


try:
    import dapla as dp
except ImportError:
    pass

import joblib
import numpy as np
import pandas as pd
from geopandas import GeoDataFrame
from pandas import DataFrame

from ..helpers import LocalFunctionError, dict_zip, dict_zip_union, in_jupyter


try:
    from ..io.dapla import exists, read_geopandas
    from ..io.write_municipality_data import write_municipality_data
except ImportError:
    pass


class Parallel:
    """Run functions in parallell.

    The main methods are 'map' and 'chunkwise'. map runs a single function for
    each item of an iterable, while chunkwise splits an iterable in roughly equal
    length parts and runs a function on each chunk.

    The class also provides functions for reading and writing files in parallell
    in dapla.

    Nothing gets printed during execution if running in a notebook. Tip:
    set processes=1 to run without parallelization when debugging.

    Note that when using the default backend 'multiprocessing', all code except for
    imports and functions should be guarded by 'if __name__ == "__main__"' to not cause
    an internal loop. This is not the case if setting backend to 'loky'. See joblib's
    documentation: https://joblib.readthedocs.io/en/latest/parallel.html#parallel-reference-documentation

    Args:
        processes: Number of parallel processes. Set to 1 to run without
            parallelization.
        backend: Defaults to "multiprocessing". Can be set to any
            backend supported by joblib's Parallel class
            (except for "multiprocessing").
        context: Start method for the processes. Defaults to 'spawn'
            to avoid frozen processes.
        **kwargs: Keyword arguments to be passed to either
            multiprocessing.Pool or joblib.Parallel, depending
            on the chosen backend.
    """

    def __init__(
        self,
        processes: int,
        backend: str = "multiprocessing",
        context: str = "spawn",
        **kwargs,
    ):
        self.processes = processes
        self.backend = backend
        self.context = context
        self.kwargs = kwargs
        self.funcs: list[functools.partial] = []
        self.results: list[Any] = []
        self._source: list[str] = []

    def map(self, func: Callable, iterable: list, **kwargs) -> list[Any]:
        """Run functions in parallel with items of an iterable as first arguemnt.

        Args:
            func: Function to be run.
            iterable: An iterable where each item will be passed to func as
                first positional argument.
            **kwargs: Keyword arguments passed to 'func'.

        Returns:
            A list of the return values of the function, one for each item in
            'iterable'.

        Examples
        --------
        Multiply each list element by 2.

        >>> iterable = [1, 2, 3]
        >>> def x2(x):
        ...     return x * 2
        >>> p = sg.Parallel(4, backend="loky")
        >>> results = p.map(x2, iterable)
        >>> results
        [2, 4, 6]

        If in Jupyter and using the multiprocessing backend,
        the function should be defined in another function
        and the code guarded by if __name__ == "__main__".

        >>> from .file import x2
        >>> if __name__ == "__main__":
        ...     p = sg.Parallel(4, backend="loky")
        ...     results = p.map(x2, iterable)
        ...     print(results)
        [2, 4, 6]

        """
        self.validate_execution(func)
        func_with_kwargs = functools.partial(func, **kwargs)

        if self.processes == 1:
            return list(map(func_with_kwargs, iterable))

        # don't use unnecessary processes
        if self.processes > len(iterable):
            processes = len(iterable)
        else:
            processes = self.processes

        if self.backend == "multiprocessing":
            with multiprocessing.get_context(self.context).Pool(
                processes, **self.kwargs
            ) as pool:
                return pool.map(func_with_kwargs, iterable)
        else:
            with joblib.Parallel(
                n_jobs=processes, backend=self.backend, **self.kwargs
            ) as parallel:
                return parallel(
                    joblib.delayed(func)(item, **kwargs) for item in iterable
                )

    def _execute(self) -> list[Any]:
        [self.validate_execution(func) for func in self.funcs]

        if self.processes == 1:
            return [func() for func in self.funcs]

        # don't use unnecessary processes
        if self.processes > len(self.funcs):
            processes = len(self.funcs)
        else:
            processes = self.processes

        if self.backend != "multiprocessing":
            with joblib.Parallel(
                n_jobs=processes, backend=self.backend, **self.kwargs
            ) as parallel:
                return parallel(joblib.delayed(func)() for func in self.funcs)

        with multiprocessing.get_context(self.context).Pool(
            processes, **self.kwargs
        ) as pool:
            results = [pool.apply_async(func) for func in self.funcs]
            return [result.get() for result in results]

    def read_pandas(
        self,
        files: list[str],
        concat: bool = True,
        ignore_index: bool = True,
        strict: bool = True,
        **kwargs,
    ) -> DataFrame | list[DataFrame]:
        """Read tabular files from a list in parallel.

        Args:
            files: List of file paths.
            concat: Whether to concat the results to a DataFrame.
            ignore_index: Defaults to True.
            strict: If True (default), all files must exist.
            **kwargs: Keyword arguments passed to dapla.read_pandas.

        Returns:
            A DataFrame, or a list of DataFrames if concat is False.
        """
        if not strict:
            files = [file for file in files if exists(file)]

        res = self.map(func=dp.read_pandas, iterable=files, **kwargs)

        return pd.concat(res, ignore_index=ignore_index) if concat else res

    def read_geopandas(
        self,
        files: list[str],
        concat: bool = True,
        ignore_index: bool = True,
        strict: bool = True,
        **kwargs,
    ) -> GeoDataFrame | list[GeoDataFrame]:
        """Read geospatial files from a list in parallel.

        Args:
            files: List of file paths.
            concat: Whether to concat the results to a GeoDataFrame.
            ignore_index: Defaults to True.
            strict: If True (default), all files must exist.
            **kwargs: Keyword arguments passed to sgis.read_geopandas.

        Returns:
            A GeoDataFrame, or a list of GeoDataFrames if concat is False.
        """
        if not strict:
            files = [file for file in files if exists(file)]
        res = self.map(func=read_geopandas, iterable=files, **kwargs)

        return pd.concat(res, ignore_index=ignore_index) if concat else res

    def chunkwise(
        self,
        func: Callable,
        iterable: Iterable,
        n: int,
        chunk_kwarg_name: str | None = None,
        **kwargs,
    ):
        """Splits an interable in n chunks and runs the function on each chunk.

        Args:
            func: Function to be run chunkwise.
            iterable: Iterable to be divided into n roughly equal length chunks.
                The chunk will be used as first argument in the function call,
                unless chunk_kwarg_name is specified.
            n: Number of chunks to divide the iterable in.
            chunk_kwarg_name: Optional keyword argument that the chunks should be
                assigned to. Defaults to None, meaning the chunk will be used as
                the first positional argument of the function.
            **kwargs: Additional keyword arguments passed to the function.

        Examples
        --------
        >>> def x2(num):
        ...     return num * 2
        >>> l = [1, 2, 3]
        >>> if __name__ == "__main__":
        ...     p = Parallel(2)
        ...     p.chunkwise(x2, l, n=3)
        ...     print(p.execute())
        [2, 4, 6]

        """
        self.validate_execution(func)

        if isinstance(iterable, (str, bytes)) or not hasattr(iterable, "__iter__"):
            raise TypeError

        if not isinstance(iterable, Sized):
            iterable = list(iterable)

        n = n if n <= len(iterable) else len(iterable)

        try:
            splitted = list(np.array_split(iterable, n))
        except Exception:

            def split(a, n):
                k, m = divmod(len(a), n)
                return [
                    a[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n)
                ]

            splitted = split(iterable, n)

        if not hasattr(self, "chunks"):
            self.chunks = []

        for chunk in splitted:
            if chunk_kwarg_name:
                partial_func = functools.partial(
                    func, **{chunk_kwarg_name: chunk}, **kwargs
                )
            else:
                partial_func = functools.partial(func, chunk, **kwargs)
            self.funcs.append(partial_func)
            self.chunks.append(chunk)
            self._source.append("chunkwise")

        return self._execute()

    def write_municipality_data(
        self,
        in_data: dict[str, str | GeoDataFrame],
        out_data: str | dict[str, str],
        municipalities: GeoDataFrame,
        with_neighbors: bool = False,
        funcdict: dict[str, Callable] | None = None,
        file_type: str = "parquet",
        muni_number_col: str = "KOMMUNENR",
        strict: bool = False,
        write_empty: bool = False,
    ):
        """Split multiple datasets into municipalities and write as separate files.

        The files will be named as the municipality number.

        Args:
            in_data: Dictionary with dataset names as keys and file paths or
                (Geo)DataFrames as values.
            out_data: Either a single folder path or a dictionary with same keys as
                'in_data' and folder paths as values. If a single folder is given,
                the 'in_data' keys will be used as subfolders.
            year: Year of the municipality numbers.
            funcdict: Dictionary with the keys of 'in_data' and functions as values.
                The functions should take a GeoDataFrame as input and return a
                GeoDataFrame.
            file_type: Defaults to parquet.
            muni_number_col: Column name that holds the municipality number. Defaults
                to KOMMUNENR.
            strict: If False (default), the dictionaries 'out_data' and 'funcdict' does
                not have to have the same length as 'in_data'.
            write_empty: If False (default), municipalities with no data will be skipped.
                If True, an empty parquet file will be written.

        """
        shared_kwds = {
            "municipalities": municipalities,
            "muni_number_col": muni_number_col,
            "file_type": file_type,
            "write_empty": write_empty,
            "with_neighbors": with_neighbors,
        }

        if isinstance(out_data, (str, Path)):
            out_data = {name: Path(out_data) / name for name in in_data}

        if funcdict is None:
            funcdict = {}

        zip_func = dict_zip if strict else dict_zip_union

        for _, data, folder, postfunc in zip_func(in_data, out_data, funcdict):
            if data is None:
                continue
            kwds = shared_kwds | {
                "data": data,
                "func": postfunc,
                "out_folder": folder,
            }
            partial_func = functools.partial(write_municipality_data, **kwds)
            self.funcs.append(partial_func)
            self._source.append("write_municipality_data")

        return self._execute()

    def validate_execution(self, func):
        if (
            func.__module__ == "__main__"
            and self.context == "spawn"
            and self.backend == "multiprocessing"
            and in_jupyter()
        ):
            raise LocalFunctionError(func)
