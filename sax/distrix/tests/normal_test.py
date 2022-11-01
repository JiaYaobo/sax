import jax.random as jrand
import jax.numpy as jnp
import numpy as np

from sax.distrix import pnorm, qnorm, rnorm


def test_rnorm():
    key = jrand.PRNGKey(19751002)
    sample_shape = (1000000, 10)
    mean = .5
    sigma = 2.
    norms = rnorm(key, sample_shape, mean, sigma)
    return (norms.mean(axis=0), norms.var(axis=0))


def test_pnorm():
    x = jnp.array([-1.96, -1.645, -1., 0, 1., 1.645, 1.96])
    p = pnorm(x)
    return p

def test_qnorm():
    q = [0.02499789, 0.04998492, 0.15865527,0.5 ,0.8413447, 0.95001507, 0.9750021]
    x = qnorm(q)
    return x

print(test_qnorm())