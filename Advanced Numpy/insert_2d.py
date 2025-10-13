import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(np.insert(arr, 1, [10,16,23], axis=0))  # Insert [10, 16, 23] at index 1 along the first axis (rows)