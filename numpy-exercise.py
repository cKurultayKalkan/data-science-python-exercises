import numpy as np

array = np.array([[1, 2, 3, 4, 5, 6, ], [7, 8, 9, 10, 11, 12]])

print(array[:, 1:4])

array = np.array([[1, 2, 3, 4, 5, 6, ], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])

print(array.ravel())

array2 = array.reshape(6, 3)

print(array2)

array3 = array.T

print(array3)

array5 = np.array([[1, 2], [3, 4], [5, 6]])

array5.resize((2, 3))

print(array5)
