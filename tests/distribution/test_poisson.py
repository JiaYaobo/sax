"""Test for poisson distribution"""
import jax.random as jrand
import numpy as np
from absl.testing import absltest
from jax._src import test_util as jtest

from stamox.distribution import dpoisson, ppoisson, rpoisson


class PoissonTest(jtest.JaxTestCase):

    def test_rpoisson(self):
        key = jrand.PRNGKey(19751002)
        sample_shape = (1000000, )
        rate = 2.5
        ts = rpoisson(key, sample_shape, rate)
        avg = ts.mean()
        var = ts.var(ddof=1)
        self.assertAllClose(avg, rate, atol=1e-2)
        self.assertAllClose(var, rate, atol=1e-2)

    def test_ppoisson(self):
        x = np.array([1., 2., 3., 4. ,5.])
        rate = 2.5
        p = ppoisson(x, rate)
        true_p = np.array(
            [0.2872975, 0.5438131, 0.7575761, 0.8911780, 0.9579790])
        self.assertArraysAllClose(p, true_p)

    # def test_qpoisson(self):
    #     q = np.array([0.4060058, 0.6766764, 0.8571235, 0.9473470, 0.9834364])
    #     x = qpoisson(q, 2.)
    #     true_x = np.array([1., 3., 5., 5., 3.])
    #     self.assertArraysAllClose(x, true_x)

    def test_dpoisson(self):
        x = np.array([1., 2. , 3., 4., 5.])
        rate = 2.5
        grads = dpoisson(x, rate)
        true_grads = np.array(
            [0.20521250 ,0.25651562 ,0.21376302 ,0.13360189 ,0.06680094])
        self.assertArraysAllClose(grads, true_grads)
    
    def test_partial_ppoisson(self):
        x = np.array([1., 2., 3., 4. ,5.])
        rate = 2.5
        p = ppoisson(rate=rate, lower_tail=False)(x)
        true_p = np.array(
            [0.7127025, 0.4561869, 0.2424239, 0.1088220, 0.0420210])
        self.assertArraysAllClose(p, true_p)
    
    def test_partial_dpoisson(self):
        x = np.array([1., 2. , 3., 4., 5.])
        rate = 2.5
        grads = dpoisson(rate=rate)(x)
        true_grads = np.array(
            [0.20521250 ,0.25651562 ,0.21376302 ,0.13360189 ,0.06680094])
        self.assertArraysAllClose(grads, true_grads)
    
    # def test_partial_qpoisson(self):
    #     q = np.array([0.4060058, 0.6766764, 0.8571235, 0.9473470, 0.9834364])
    #     x = qpoisson(rate=2.)(q)
    #     true_x = np.array([1., 3., 5., 5., 3.])
    #     self.assertArraysAllClose(x, true_x)
    
    def test_partial_rpoisson(self):
        key = jrand.PRNGKey(19751002)
        sample_shape = (1000000, )
        rate = 2.5
        ts = rpoisson(rate=rate)(key, sample_shape=sample_shape)
        avg = ts.mean()
        var = ts.var(ddof=1)
        self.assertAllClose(avg, rate, atol=1e-2)
        self.assertAllClose(var, rate, atol=1e-2)



if __name__ == '__main__':
    absltest.main(testLoader=jtest.JaxTestLoader())