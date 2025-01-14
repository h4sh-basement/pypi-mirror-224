from __future__ import annotations

from typing import Any

import pandas as pd
import polars as pl
import pytest

import dataframe_api_compat.pandas_standard
import dataframe_api_compat.polars_standard


def convert_to_standard_compliant_dataframe(df: pd.DataFrame | pl.DataFrame) -> Any:
    # todo: type return
    if isinstance(df, pd.DataFrame):
        return (
            dataframe_api_compat.pandas_standard.convert_to_standard_compliant_dataframe(
                df, None
            )
        )
    elif isinstance(df, (pl.DataFrame, pl.LazyFrame)):
        return (
            dataframe_api_compat.polars_standard.convert_to_standard_compliant_dataframe(
                df, None
            )
        )
    else:
        raise AssertionError(f"Got unexpected type: {type(df)}")


def convert_to_standard_compliant_column(ser: pd.Series[Any] | pl.Series) -> Any:
    # todo: type return
    if isinstance(ser, pd.Series):
        return dataframe_api_compat.pandas_standard.convert_to_standard_compliant_column(
            ser, None
        )
    elif isinstance(ser, pl.Series):
        return dataframe_api_compat.polars_standard.convert_to_standard_compliant_column(
            ser, None
        )
    else:
        raise AssertionError(f"Got unexpected type: {type(ser)}")


def convert_dataframe_to_pandas_numpy(df: pd.DataFrame) -> pd.DataFrame:
    conversions = {
        "boolean": "bool",
        "Int64": "int64",
        "Float64": "float64",
    }
    for nullable, numpy in conversions.items():
        df = df.astype({key: numpy for key in df.columns[df.dtypes == nullable]})
    return df


def convert_series_to_pandas_numpy(ser: pd.Series) -> pd.Series:  # type: ignore[type-arg]
    conversions = {
        "boolean": "bool",
        "Int64": "int64",
        "Int32": "int32",
        "Int16": "int16",
        "Int8": "int8",
        "UInt64": "uint64",
        "UInt32": "uint32",
        "UInt16": "uint16",
        "UInt8": "uint8",
        "Float64": "float64",
        "Float32": "float32",
        "string": "object",
    }
    for nullable, numpy in conversions.items():
        if ser.dtype == nullable:
            ser = ser.astype(numpy)  # type: ignore[call-overload]
    return ser


def integer_dataframe_1(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, dtype="int64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, dtype="Int64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def integer_dataframe_2(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [1, 2, 4], "b": [4, 2, 6]}, dtype="int64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1, 2, 4], "b": [4, 2, 6]}, dtype="Int64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"a": [1, 2, 4], "b": [4, 2, 6]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [1, 2, 4], "b": [4, 2, 6]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def integer_dataframe_3(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame(
            {"a": [1, 2, 3, 4, 5, 6, 7], "b": [7, 6, 5, 4, 3, 2, 1]}, dtype="int64"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame(
            {"a": [1, 2, 3, 4, 5, 6, 7], "b": [7, 6, 5, 4, 3, 2, 1]}, dtype="Int64"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7], "b": [7, 6, 5, 4, 3, 2, 1]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [1, 2, 3, 4, 5, 6, 7], "b": [7, 6, 5, 4, 3, 2, 1]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def integer_dataframe_4(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame(
            {"key": [1, 1, 2, 2], "b": [1, 2, 3, 4], "c": [4, 5, 6, 7]}, dtype="int64"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame(
            {"key": [1, 1, 2, 2], "b": [1, 2, 3, 4], "c": [4, 5, 6, 7]}, dtype="Int64"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"key": [1, 1, 2, 2], "b": [1, 2, 3, 4], "c": [4, 5, 6, 7]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"key": [1, 1, 2, 2], "b": [1, 2, 3, 4], "c": [4, 5, 6, 7]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def integer_dataframe_5(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [1, 1], "b": [4, 3]}, dtype="int64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1, 1], "b": [4, 3]}, dtype="Int64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"a": [1, 1], "b": [4, 3]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":  # pragma: no cover
        df = pl.LazyFrame({"a": [1, 1], "b": [4, 3]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def integer_dataframe_6(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [1, 1, 1, 2, 2], "b": [4, 4, 3, 1, 2]}, dtype="int64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1, 1, 1, 2, 2], "b": [4, 4, 3, 1, 2]}, dtype="Int64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"a": [1, 1, 1, 2, 2], "b": [4, 4, 3, 1, 2]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [1, 1, 1, 2, 2], "b": [4, 4, 3, 1, 2]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def nan_dataframe_1(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [1.0, 2.0, float("nan")]}, dtype="float64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1.0, 2.0, 0.0]}, dtype="Float64")
        other = pd.DataFrame({"a": [1.0, 1.0, 0.0]}, dtype="Float64")
        return convert_to_standard_compliant_dataframe(df / other)
    if library == "polars":
        df = pl.DataFrame({"a": [1.0, 2.0, float("nan")]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [1.0, 2.0, float("nan")]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def nan_dataframe_2(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [0.0, 1.0, float("nan")]}, dtype="float64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [0.0, 1.0, 0.0]}, dtype="Float64")
        other = pd.DataFrame({"a": [1.0, 1.0, 0.0]}, dtype="Float64")
        return convert_to_standard_compliant_dataframe(df / other)
    if library == "polars":
        df = pl.DataFrame({"a": [0.0, 1.0, float("nan")]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [0.0, 1.0, float("nan")]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def null_dataframe_1(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [1.0, 2.0, float("nan")]}, dtype="float64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1.0, 2.0, pd.NA]}, dtype="Float64")
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"a": [1.0, 2.0, None]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [1.0, 2.0, None]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def null_dataframe_2(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame(
            {"a": [1.0, -1.0, float("nan")], "b": [1.0, -1.0, float("nan")]},
            dtype="float64",
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame(
            {"a": [1.0, 0.0, pd.NA], "b": [1.0, 1.0, pd.NA]}, dtype="Float64"
        )
        return convert_to_standard_compliant_dataframe(df / df)
    if library == "polars":
        df = pl.DataFrame({"a": [1.0, float("nan"), None], "b": [1.0, 1.0, None]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [1.0, float("nan"), None], "b": [1.0, 1.0, None]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def bool_dataframe_1(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame(
            {"a": [True, True, False], "b": [True, True, True]}, dtype="bool"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame(
            {"a": [True, True, False], "b": [True, True, True]}, dtype="boolean"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"a": [True, True, False], "b": [True, True, True]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [True, True, False], "b": [True, True, True]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def bool_dataframe_2(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame(
            {
                "key": [1, 1, 2, 2],
                "b": [False, True, True, True],
                "c": [True, False, False, False],
            }
        ).astype({"key": "int64", "b": "bool", "c": "bool"})
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame(
            {
                "key": [1, 1, 2, 2],
                "b": [False, True, True, True],
                "c": [True, False, False, False],
            }
        ).astype({"key": "Int64", "b": "boolean", "c": "boolean"})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame(
            {
                "key": [1, 1, 2, 2],
                "b": [False, True, True, True],
                "c": [True, False, False, False],
            }
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame(
            {
                "key": [1, 1, 2, 2],
                "b": [False, True, True, True],
                "c": [True, False, False, False],
            }
        )
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def bool_dataframe_3(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame(
            {"a": [False, False], "b": [False, True], "c": [True, True]}, dtype="bool"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame(
            {"a": [False, False], "b": [False, True], "c": [True, True]}, dtype="boolean"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"a": [False, False], "b": [False, True], "c": [True, True]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [False, False], "b": [False, True], "c": [True, True]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def bool_dataframe_4(library: str) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame(
            {"a": [False, True, False], "b": [True, True, True]}, dtype="bool"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "pandas-nullable":
        df = pd.DataFrame(
            {"a": [False, True, False], "b": [True, True, True]}, dtype="boolean"
        )
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars":
        df = pl.DataFrame({"a": [False, True, False], "b": [True, True, True]})
        return convert_to_standard_compliant_dataframe(df)
    if library == "polars-lazy":
        df = pl.LazyFrame({"a": [False, True, False], "b": [True, True, True]})
        return convert_to_standard_compliant_dataframe(df)
    raise AssertionError(f"Got unexpected library: {library}")


def integer_series_1(library: str, request: pytest.FixtureRequest) -> Any:
    ser: Any
    if library == "pandas-numpy":
        ser = pd.Series([1, 2, 3])
        return convert_to_standard_compliant_column(ser)
    if library == "pandas-nullable":
        ser = pd.Series([1, 2, 3], dtype="Int64")
        return convert_to_standard_compliant_column(ser)
    if library == "polars":
        ser = pl.Series([1, 2, 3])
        return convert_to_standard_compliant_column(ser)
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def integer_series_3(library: str, request: pytest.FixtureRequest) -> object:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [1, 2, 4]}, dtype="int64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1, 2, 4]}, dtype="Int64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [1, 2, 4]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":  # pragma: no cover
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def integer_series_5(library: str, request: pytest.FixtureRequest) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [1, 1, 4]}, dtype="int64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1, 1, 4]}, dtype="Int64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [1, 1, 4]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def float_series_1(library: str, request: pytest.FixtureRequest) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [2.0, 3.0]}, dtype="float64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [2.0, 3.0]}, dtype="Float64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [2.0, 3.0]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def float_series_2(library: str, request: pytest.FixtureRequest) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [2.0, 1.0]}, dtype="float64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [2.0, 1.0]}, dtype="Float64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [2.0, 1.0]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":  # pragma: no cover
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def float_series_3(library: str, request: pytest.FixtureRequest) -> object:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [float("nan"), 2.0]}, dtype="float64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [0.0, 2.0]}, dtype="Float64")
        other = pd.DataFrame({"a": [0.0, 1.0]}, dtype="Float64")
        return convert_to_standard_compliant_dataframe(df / other).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [float("nan"), 2.0]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":  # pragma: no cover
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def float_series_4(library: str, request: pytest.FixtureRequest) -> object:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [1.0, float("nan")]}, dtype="float64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1.0, 0.0]}, dtype="Float64")
        other = pd.DataFrame({"a": [1.0, 0.0]}, dtype="Float64")
        return convert_to_standard_compliant_dataframe(df / other).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [1.0, float("nan")]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def bool_series_1(library: str, request: pytest.FixtureRequest) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [True, False, True]}, dtype="bool")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [True, False, True]}, dtype="boolean")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [True, False, True]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def bool_series_2(library: str, request: pytest.FixtureRequest) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [True, False, False]}, dtype="bool")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [True, False, False]}, dtype="boolean")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [True, False, False]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":  # pragma: no cover
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def nan_series_1(library: str, request: pytest.FixtureRequest) -> Any:
    df: Any
    if library == "pandas-numpy":
        df = pd.DataFrame({"a": [0.0, 1.0, float("nan")]}, dtype="float64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [0.0, 1.0, 0.0]}, dtype="Float64")
        other = pd.DataFrame({"a": [1.0, 1.0, 0.0]}, dtype="Float64")
        return convert_to_standard_compliant_dataframe(df / other).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [0.0, 1.0, float("nan")]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def null_series_1(library: str, request: pytest.FixtureRequest) -> Any:
    df: Any
    if library == "pandas-numpy":
        mark = pytest.mark.xfail()
        request.node.add_marker(mark)
    if library == "pandas-nullable":
        df = pd.DataFrame({"a": [1.0, 2.0, pd.NA]}, dtype="Float64")
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars":
        df = pl.DataFrame({"a": [1.0, 2.0, None]})
        return convert_to_standard_compliant_dataframe(df).get_column_by_name("a")
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    raise AssertionError(f"Got unexpected library: {library}")


def interchange_to_pandas(result: Any, library: str) -> pd.DataFrame:
    df = result.dataframe.collect() if library == "polars-lazy" else result.dataframe
    return pd.api.interchange.from_dataframe(df)


def maybe_collect(result: Any, library: str) -> Any:
    df = result.dataframe.collect() if library == "polars-lazy" else result.dataframe
    return df
