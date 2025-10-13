import numpy as np
arr = np.array([1,2,np.nan,4,5,np.nan])
print(np.nan_to_num(arr))  # Output: [ 1.  2.  0.  4.  5.  0.]