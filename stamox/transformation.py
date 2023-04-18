import jax.numpy as jnp
from jax import lax
from jaxtyping import ArrayLike

from .core import partial_pipe_jit, pipe_jit


@partial_pipe_jit
def boxcox(x: ArrayLike, lmbda: ArrayLike, dtype=jnp.float32) -> ArrayLike:
    """Computes the Box-Cox transformation of a given array.

    Args:
        x: An array-like object to be transformed.
        lmbda: An array-like object containing the lambda values for the transformation.

    Returns:
        The boxcox transformed array.

    Example:
        >>> from stamox.transformation import boxcox
        >>> import jax.numpy as jnp
        >>> x = jnp.array([1, 2, 3, 4, 5], dtype=jnp.float32)
        >>> lmbda = jnp.array([0, 0, 0, 0, 0], dtype=jnp.float32)
        >>> boxcox(x, lmbda)
        Array([0.        , 0.6931472 , 1.0986123 , 1.3862944 , 1.6094378 ], dtype=float32)
    """
    x = jnp.asarray(x, dtype=dtype)
    lmbda = jnp.asarray(lmbda, dtype=dtype)
    return lax.select(lmbda == 0, jnp.log(x), (jnp.power(x, lmbda) - 1) / lmbda)


@partial_pipe_jit
def z_fisher(rho: ArrayLike, dtype=jnp.float32) -> ArrayLike:
    """Computes the Fisher z-transform of a given array.

    Args:
        rho: An array-like object to be transformed.

    Returns:
        The Fisher z-transformed array.

    Example:
        >>> from stamox.transformation import z_fisher
        >>> import jax.numpy as jnp
        >>> rho = jnp.array([0.1, 0.2, 0.3, 0.4, 0.5], dtype=jnp.float32)
        >>> z_fisher(rho)
        Array([0.10033537, 0.2013589 , 0.30469212, 0.41073018, 0.51991177], dtype=float32)
    """
    rho = jnp.clip(rho, -1.0, 1.0).astype(dtype)
    return jnp.arctanh(rho)
