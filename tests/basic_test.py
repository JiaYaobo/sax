from stamox.core import StateFunc, Functional, pipe_jit,  make_partial_pipe, make_pipe, partial_pipe_jit
import jax.random as jrandom
import jax.numpy as jnp
from functools import partial
from jax import jit, vmap, grad


x = jnp.array([1. ,2. ,3.])


@make_pipe
def f(x):
    return x**2

@make_pipe
def g(x):
    return x + 1

def m(x):
    return x

@make_partial_pipe
def k(x, y):
    return x ** 3 + y


h = f >> g >> m >> k(y=1.)

vmap_h = vmap(h, in_axes=(0))

vmap_f = vmap(f, in_axes=(0))

print(h(x))