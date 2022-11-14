import jax.numpy as jnp
import jax.tree_util as jtu

from jax import jit, vmap, lax
from jax.scipy.special import gammaln

from ..util import zero_dim_to_1_dim_array


def choose(n ,k):
    k = jnp.asarray(k ,dtype=jnp.int32)
    k = zero_dim_to_1_dim_array(k)
    return vmap(_choose, in_axes=(None, 0))(n, k)


@jtu.Partial(jit)
def _cal_choose(n, k):
    log_kfrac = gammaln(k + 1)
    log_nfrac = gammaln(n + 1)
    log_n_kfrac = gammaln(n-k + 1)
    comb = jnp.exp(log_nfrac - log_kfrac - log_n_kfrac)
    comb = jnp.round(comb)


@jtu.Partial(jit)
def _choose(n ,k):
    # should be modified to avoid redudant computation
    if_illegal = jnp.where(jnp.logical_or(k >n, k<0) , 1, 0)
    # log_kfrac = gammaln(k + 1)
    # log_nfrac = gammaln(n + 1)
    # log_n_kfrac = gammaln(n-k + 1)
    # comb = jnp.exp(log_nfrac - log_kfrac - log_n_kfrac)
    # comb = jnp.round(comb)
    func1 = lambda : jnp.asarray(0, dtype=jnp.int32)
    func2 = lambda nn, kk: _cal_choose(nn, kk) 
    
    return jnp.asarray(lax.cond(if_illegal, func1, func2, n, k))
