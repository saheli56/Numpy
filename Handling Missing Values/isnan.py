import numpy as np
arr = np.array([1,2,np.nan,4,5,np.nan])
print(np.isnan(arr))  # Output: [False False  True False False  True]