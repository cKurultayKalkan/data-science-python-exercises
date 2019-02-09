import numpy as np

array = np.array([[1, 2, 3, 4, 5, 6, ], [7, 8, 9, 10, 11, 12]])

print("array sliced")
print(array[:, 1:4])

array = np.array([[1, 2, 3, 4, 5, 6, ], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]])
print("array")
print(array)

print("*************")
print("array ravel")
print(array.ravel())
print("*************")
print("*************")
array2 = array.reshape(6, 3)
print("array2 reshape")
print(array2)
array3 = array.T
print("*************")
print("array3, transpoze of array")
print(array3)

array4 = np.array([[3, 6], [9, 12], [15, 18]])
print("*************")
print("array4")
print(array4)
print("shape: ", array4.shape)
print("dimension: ", array4.ndim)
print("data type: ", array4.dtype.name)
print("size: ", array4.size)
print("type: ", type(array4))

print(np.ones((3, 4)))
print(np.empty((2, 3)))

a = np.arange(10, 50, 5)
print(a)

array5 = np.array([[1, 2], [3, 4], [5, 6]])

array5.resize((2, 3))

print("*************")
print("array5")
print(array5)

array6 = np.column_stack((array2, array3))

print("*************")
print("array2")
print(array2)
print("array3")
print(array3)
print("array6 column_stack array2 and array3")
print(array6)

array7 = np.array([[1, 2], [3, 4]])

array8 = np.array([[-1, -2], [-3, -4]])

print("array7")
print(array7)
print("array8")
print(array8)

print("vertical concat")
print(np.vstack((array7, array8)))

print("horizontal concat")
print(np.hstack((array7, array8)))

print("column stack")
print(np.column_stack((array7, array8)))
