import numpy as np
np.random.seed(0)
class Feed_Forword:
  
  def __init__(self, number_of_inputs, number_of_neurons):
    self.layer = np.random.rand(number_of_inputs, number_of_neurons)
    self.bias = np.zeros((number_of_inputs))
  def train_ff(self, inputs, hidden):
    self.output = np.dot(hidden, inputs) + self.bias


first_object = Feed_Forword(3, 4)
first_object
print('first_object.inputs', first_object.inputs)
print('first_object.bias', first_object.bias)