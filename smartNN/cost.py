import theano.tensor as T
import theano

class Cost(object):
    """
    Cost inherits MLP so that cost can make use of the 
    """
    def __init__(self, type = 'nll'):
        self.type = type
        
    def get_accuracy(self, y, y_pred):
        """Return a float representing the number of errors in the minibatch
        over the total number of examples of the minibatch ; zero one
        loss over the size of the minibatch

        :type y: theano.tensor.TensorType
        :param y: corresponds to a vector that gives for each example the
                  correct label
        """

        # check if y has same dimension of y_pred
        if y.ndim != y_pred.ndim:
            raise TypeError('y should have the same shape as self.y_pred',
                ('y', y.type, 'y_pred', y_pred.type))

        return T.eq(y_pred.argmax(axis=1), 
                    y.argmax(axis=1)).sum(dtype=theano.config.floatX) / y.shape[0]

    
    def positives(self, y, y_pred):
        """
        return the number of correctly predicted examples in a batch
        """
        return T.eq(y_pred.argmax(axis=1), y.argmax(axis=1)).sum(dtype=theano.config.floatX)
    
    def get_batch_cost(self, y, y_pred):
        return getattr(self, '_batch_cost_' + self.type)(y, y_pred)
    
    def _batch_cost_nll(self, y, y_pred):
        """
        return the total cost of all the examples in a batch
        """
        return T.sum(T.log(y_pred)[T.arange(y.shape[0]), y.argmin(axis=1)])
    
    def confusion_matrix(self, y, y_pred):
        pass
            
    def get_cost(self, y, y_pred):
        return getattr(self, '_cost_' + self.type)(y, y_pred)
    
    def _cost_nll(self, y, y_pred):
        return -T.mean(T.log(y_pred)[T.arange(y.shape[0]), y.argmin(axis=1)])
    
    def _cost_mse(self, y, y_pred):
        return T.mean(T.sqr(y - y_pred))
    
    def _cost_error(self, y, y_pred):
        return T.mean(T.neq(y_pred.argmax(axis=1), y.argmax(axis=1)), dtype=theano.config.floatX)
    
        
    