# Python function that takes two numpy arrays
# and finds the dot product. Numpy contains
# a dot() function, but this is a custom
# function for practice.
# Peter Menchu 2023
import numpy as np


def dotProduct(a, b):
    # a, b need to be numpy arrays of the same length
    if not (isinstance(a, np.ndarray) and isinstance(b, np.ndarray)):
        return "One of the arrays is not a numpy array."
    elif not (len(a) == len(b)):
        return "The arrays aren't the same length."
    else:
        # multiply each element and get their sum
        return sum(a * b)


c = np.array([6, 3, 1])
d = np.array([2, 4, 6])

dotProd_cd = dotProduct(c, d)

if not isinstance(dotProd_cd, str):
    print("Dot product of these arrays is ", dotProd_cd)
else:
    print(dotProd_cd)

# Peter Menchu 2023
