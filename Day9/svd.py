import numpy as np

A = np.array([
    [3, 2],
    [2, 3]
])

U, S, VT = np.linalg.svd(A)

print("U:")
print(U)

print("\nSingular Values:")
print(S)

print("\nVT:")
print(VT)