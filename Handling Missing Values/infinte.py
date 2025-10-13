import numpy as np
arr = np.array([1,2,np.inf,4,5,-np.inf])
print(np.isinf(arr))  # Output: [False False  True False False  True]