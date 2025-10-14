import numpy as np
arr = np.array([1, 2, np.inf, 4, 5, -np.inf])
print(np.isinf(arr))  # Output: [False False  True False False  True]

cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)
print(cleaned_arr)  # Output: [   1    2 1000    4    5 -1000]