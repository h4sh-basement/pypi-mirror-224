# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE
__all__ = ("backend",)
from awkward._backends.dispatch import backend_of
from awkward._dispatch import high_level_function


@high_level_function()
def backend(*arrays):
    """
    Args:
        arrays: Array-like data (anything #ak.to_layout recognizes).

    Returns the names of the backend used by `arrays`. This name may be

    * `"cpu"` for arrays backed by NumPy;
    * `"cuda"` for arrays backed by CuPy;
    * `"jax"` for arrays backed by JAX;
    * `"typetracer"` for arrays without any data;
    * None if the objects are not Awkward, NumPy, JAX, CuPy, or typetracer arrays (e.g.
      Python numbers, booleans, strings).

    See #ak.to_backend.
    """
    # Dispatch
    yield arrays

    # Implementation
    return _impl(arrays)


def _impl(arrays) -> str:
    backend_impl = backend_of(*arrays, default=None)
    return backend_impl.name
