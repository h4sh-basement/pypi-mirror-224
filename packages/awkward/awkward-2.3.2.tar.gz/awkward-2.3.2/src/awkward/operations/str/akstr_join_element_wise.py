# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

__all__ = ("join_element_wise",)

import awkward as ak
from awkward._behavior import behavior_of
from awkward._dispatch import high_level_function
from awkward._layout import wrap_layout


@high_level_function(module="ak.str")
def join_element_wise(*arrays, highlevel=True, behavior=None):
    """
    Args:
        arrays: Array-like data (anything #ak.to_layout recognizes).
        highlevel (bool): If True, return an #ak.Array; otherwise, return
            a low-level #ak.contents.Content subclass.
        behavior (None or dict): Custom #ak.behavior for the output array, if
            high-level.

    Broadcasts and concatenates all but the last array of strings in `arrays`;
    the last is used as a separator.

    Note: this function does not raise an error if the `array` does not
    contain any string or bytestring data.

    Requires the pyarrow library and calls
    [pyarrow.compute.binary_join_element_wise](https://arrow.apache.org/docs/python/generated/pyarrow.compute.binary_join_element_wise.html).

    Unlike Arrow's `binary_join_element_wise`, this function has no `null_handling`
    and `null_replacement` arguments. This function's behavior is like
    `null_handling="emit_null"` (Arrow's default). The other cases can be implemented
    with Awkward slices, #ak.drop_none, and #ak.fill_none.

    See also: #ak.str.join.
    """
    # Dispatch
    yield arrays

    # Implementation
    return _impl(arrays, highlevel, behavior)


def _impl(arrays, highlevel, behavior):
    import awkward._connect.pyarrow  # noqa: F401, I001
    from awkward.operations.ak_from_arrow import from_arrow
    from awkward.operations.ak_to_arrow import to_arrow

    import pyarrow.compute as pc

    if len(arrays) < 1:
        raise TypeError("at least one array is required")

    layouts = [ak.to_layout(x) for x in arrays]
    behavior = behavior_of(*arrays, behavior=behavior)

    def action(layouts, **kwargs):
        if all(
            x.is_list and x.parameter("__array__") in ("string", "bytestring")
            for x in layouts
        ):
            return (
                from_arrow(
                    pc.binary_join_element_wise(
                        *[to_arrow(x, extensionarray=False) for x in layouts]
                    ),
                    highlevel=False,
                ),
            )

    (out,) = ak._broadcasting.broadcast_and_apply(layouts, action, behavior)

    return wrap_layout(out, highlevel=highlevel, behavior=behavior)
