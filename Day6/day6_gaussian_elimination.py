import numpy as np


def gaussian_elimination(A, b):
    n = len(A)

    # Make copies so we do not modify the original A and b
    A = [row[:] for row in A]
    b = b[:]

    # Forward elimination
    for pivot_row in range(n):
        pivot = A[pivot_row][pivot_row]

        if pivot == 0:
            raise ValueError("Zero pivot found. This simple version cannot solve it.")

        for row in range(pivot_row + 1, n):
            factor = A[row][pivot_row] / pivot

            for col in range(pivot_row, n):
                A[row][col] = A[row][col] - factor * A[pivot_row][col]

            b[row] = b[row] - factor * b[pivot_row]

    # Back substitution
    x = [0] * n

    for row in range(n - 1, -1, -1):
        total = 0

        for col in range(row + 1, n):
            total += A[row][col] * x[col]

        x[row] = (b[row] - total) / A[row][row]

    return x


A = [
    [1, 1, 1],
    [2, -1, 1],
    [1, 2, -1]
]

b = [9, 8, 3]

solution = gaussian_elimination(A, b)

print("Solution:")
print(solution)


A_np = np.array(A, dtype=float)
b_np = np.array(b, dtype=float)

numpy_solution = np.linalg.solve(A_np, b_np)

print("NumPy solution:")
print(numpy_solution)

print("Determinant:")
print(np.linalg.det(A_np))

print("Inverse:")
print(np.linalg.inv(A_np))

print("A inverse multiplied by b:")
print(np.linalg.inv(A_np) @ b_np)
a = np.array([1, 0, 0])
b_vector = np.array([0, 1, 0])

cross_result = np.cross(a, b_vector)

print("Cross product:")
print(cross_result)