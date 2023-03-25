import jax.random as jrandom

import jax.numpy as jnp

from stamox.sample import bootstrap_sample
from stamox.basic import mean



key = jrandom.PRNGKey(0)

x = jrandom.normal(key=key, shape=(10, 10))

h = bootstrap_sample(num_samples=3, key=key) >> mean(axis=1)

print(h(x))
