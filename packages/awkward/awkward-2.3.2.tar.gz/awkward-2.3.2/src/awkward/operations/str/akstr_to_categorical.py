# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

__all__ = ("to_categorical",)

import awkward as ak
from awkward._behavior import behavior_of
from awkward._dispatch import high_level_function
from awkward._layout import wrap_layout


@high_level_function(module="ak.str")
def to_categorical(array, *, highlevel=True, behavior=None):
    """
    Args:
        array: Array-like data (anything #ak.to_layout recognizes).
        highlevel (bool): If True, return an #ak.Array; otherwise, return
            a low-level #ak.contents.Content subclass.
        behavior (None or dict): Custom #ak.behavior for the output array, if
            high-level.

    Returns a dictionary-encoded version of the given array of strings.
    Creates a categorical dataset, which has the following properties:

       * only distinct values (categories) are stored in their entirety,
       * pointers to those distinct values are represented by integers
         (an #ak.contents.IndexedArray or #ak.contents.IndexedOptionArray
         labeled with parameter `"__array__" = "categorical"`.

    This is equivalent to R's "factor", and Pandas's "categorical".
    It differs from generic uses of #ak.contents.IndexedArray and
    #ak.contents.IndexedOptionArray in Awkward Arrays by the guarantee of no
    duplicate categories and the `"categorical"` parameter.


    Unlike Arrow's `dictionary_encode`, this function has no `null_handling`
    argument. This function's behavior is like`null_handling="mask"` (Arrow's default).
    It is not possible to encode null values in Awkward Array, as #ak.contents.IndexedOptionArray
    cannot contain an option type node.

    Note: this function does not raise an error if the `array` does not
    contain any string or bytestring data.

    Requires the pyarrow library and calls
    [pyarrow.compute.dictionary_encode](https://arrow.apache.org/docs/python/generated/pyarrow.compute.dictionary_encode.html).
    """
    # Dispatch
    yield (array,)

    # Implementation
    return _impl(array, highlevel, behavior)


def _impl(array, highlevel, behavior):
    from awkward._connect.pyarrow import import_pyarrow_compute

    pc = import_pyarrow_compute("ak.str.to_categorical")
    behavior = behavior_of(array, behavior=behavior)

    def action(layout, **kwargs):
        if layout.is_list and layout.parameter("__array__") in {"string", "bytestring"}:
            result = ak.from_arrow(
                pc.dictionary_encode(ak.to_arrow(layout, extensionarray=False)),
                highlevel=False,
            )
            # Arrow _always_ adds an option here, even though we know that
            # no values are null. Therefore, we can safely replace the indexed
            # option-type with an indexed type.
            assert isinstance(result, ak.contents.IndexedOptionArray)
            return ak.contents.IndexedArray(
                result.index, result.content, parameters=result._parameters
            )

    out = ak._do.recursively_apply(
        ak.operations.to_layout(array),
        action,
        behavior,
    )

    return wrap_layout(out, behavior, highlevel)
