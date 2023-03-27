"""Test for Durbin-Watson test"""
from absl.testing import absltest

from jax._src import test_util as jtest
import numpy as np
from statsmodels.stats.stattools import durbin_watson
from equinox import filter_jit

from stamox.hypothesis import durbin_watson_test
from stamox.core import Pipeable

class DurbinWastonTest(jtest.JaxTestCase):
    def test_durbin_waston(self):
        x = np.array([0.1, 0.2, 0.3] * 50, dtype=np.float32)
        state = durbin_watson_test(x)
        self.assertAllClose(state.statistic, np.array([durbin_watson(x)]), atol=1e-3)
        
    def test_pipe_durbin_waston(self):
        x = np.array([0.1, 0.2, 0.3] * 50, dtype=np.float32)
        h = Pipeable(x) >> durbin_watson_test
        state = h()
        self.assertAllClose(state.statistic, np.array([durbin_watson(x)]), atol=1e-3)
    
    def test_pipe_durbin_waston_jit(self):
        x = np.array([0.1, 0.2, 0.3] * 50, dtype=np.float32)
        h = filter_jit(Pipeable(x) >> durbin_watson_test)
        state = h()
        self.assertAllClose(state.statistic, np.array([durbin_watson(x)]), atol=1e-3)

if __name__ == "__main__":
    absltest.main(testLoader=jtest.JaxTestLoader())