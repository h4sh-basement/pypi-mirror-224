from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from tests.utils import convert_series_to_pandas_numpy
from tests.utils import integer_dataframe_1
from tests.utils import interchange_to_pandas


@pytest.mark.parametrize(
    ("namespace_dtype", "pandas_dtype"),
    [
        ("Int64", "int64"),
        ("Int32", "int32"),
        ("Int16", "int16"),
        ("Int8", "int8"),
        ("UInt64", "uint64"),
        ("UInt32", "uint32"),
        ("UInt16", "uint16"),
        ("UInt8", "uint8"),
    ],
)
def test_column_from_1d_array(
    library: str, request: pytest.FixtureRequest, namespace_dtype: str, pandas_dtype: str
) -> None:
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    ser = integer_dataframe_1(library).get_column_by_name("a")
    namespace = ser.__column_namespace__()
    arr = np.array([1, 2, 3])
    result = namespace.dataframe_from_dict(
        {
            "result": namespace.column_from_1d_array(
                arr, name="result", dtype=getattr(namespace, namespace_dtype)()
            )
        }
    )
    result_pd = interchange_to_pandas(result, library)["result"]
    expected = pd.Series([1, 2, 3], name="result", dtype=pandas_dtype)
    pd.testing.assert_series_equal(result_pd, expected)


@pytest.mark.parametrize(
    ("namespace_dtype", "pandas_dtype"),
    [
        ("String", "object"),
    ],
)
def test_column_from_1d_array_string(
    library: str, request: pytest.FixtureRequest, namespace_dtype: str, pandas_dtype: str
) -> None:
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    ser = integer_dataframe_1(library).get_column_by_name("a")
    namespace = ser.__column_namespace__()
    arr = np.array(["a", "b", "c"])
    result = namespace.dataframe_from_dict(
        {
            "result": namespace.column_from_1d_array(
                arr, name="result", dtype=getattr(namespace, namespace_dtype)()
            )
        }
    )
    result_pd = interchange_to_pandas(result, library)["result"]
    result_pd = convert_series_to_pandas_numpy(result_pd)
    expected = pd.Series(["a", "b", "c"], name="result", dtype=pandas_dtype)
    pd.testing.assert_series_equal(result_pd, expected)
