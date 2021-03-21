inputs = [1, -2, 3, -4]

weights = [
          [-2.3, -2.2, 1.3],
          [4.3, 2.1, 1.2],
          [-1.3, 3.5, -3.2],
          [-1.3, 3.5, -3.2],
          ]

bias = [1, 3, 4]


import numpy as np

output = np.dot(np.array(weights).T, inputs) + bias

print(output)