import numpy as np


A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

v = np.array([5, 6])

print("A:")
print(A)

print("B:")
print(B)

print("Transpose of A:")
print(A.T)

print("A multiplied by vector v:")
print(A @ v)

print("A multiplied by B:")
print(A @ B)

print("2x2 Identity matrix:")
print(np.eye(2))

print("A multiplied by identity:")
print(A @ np.eye(2))