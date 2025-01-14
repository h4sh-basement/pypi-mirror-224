# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE
__all__ = ("from_arrow_schema",)
from awkward._dispatch import high_level_function
from awkward._nplikes.numpylike import NumpyMetadata

np = NumpyMetadata.instance()


@high_level_function()
def from_arrow_schema(schema):
    """
    Args:
        schema (`pyarrow.Schema`): Apache Arrow schema to convert into an Awkward Form.

    Converts an Apache Arrow schema into an Awkward Form.

    See also #ak.to_arrow, #ak.to_arrow_table, #ak.from_arrow, #ak.to_parquet, #ak.from_parquet.
    """
    return _impl(schema)


def _impl(schema):
    import awkward._connect.pyarrow

    return awkward._connect.pyarrow.form_handle_arrow(schema, pass_empty_field=True)
