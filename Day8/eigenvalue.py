import numpy as np

A = np.array([
    [4, 1],
    [2, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print()

print("Eigenvectors:")
print(eigenvectors)