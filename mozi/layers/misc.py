
"""
Functionality : Define the noise that is to be added to each layer
"""

import theano
import theano.tensor as T
from mozi.layers.template import Template

class Flatten(Template):

    def _test_fprop(self, state_below):
        return self._train_fprop(state_below)

    def _train_fprop(self, state_below):
        size = T.prod(state_below.shape) / state_below.shape[0]
        nshape = (state_below.shape[0], size)
        return T.reshape(state_below, nshape)


class Reshape(Template):

    def __init__(self, dims):
        self.params = []
        self.dims = dims

    def _test_fprop(self, state_below):
        return self._train_fprop(state_below)

    def _train_fprop(self, state_below):
        nshape = (state_below.shape[0],) + self.dims
        return T.reshape(state_below, nshape)


class Transform(Template):

    def __init__(self, dims):
        '''
        Reshaping the data such that the first dim alters when the rest of the
        dim is altered. If X of shape (a, b, c, d) and input dims of shape (d, e),
        then return shape will be (a*b*c*d/(d*e), d, e). Useful for tranforming
        data in RNN/LSTM with mlp layers before recurrent layers.
        '''
        self.params = []
        self.dims = dims

    def _test_fprop(self, state_below):
        return self._train_fprop(state_below)

    def _train_fprop(self, state_below):
        first_dim = T.prod(state_below.shape) / np.prod(self.dims)
        return T.reshape(state_below, (first_dim,)+self.dims)
