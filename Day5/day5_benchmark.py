import time
import random
import numpy as np


def matmul(A, B):
    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Matrix multiplication is not allowed")

    result = []

    for i in range(rows_A):
        new_row = []

        for j in range(cols_B):
            total = 0

            for k in range(cols_A):
                total += A[i][k] * B[k][j]

            new_row.append(total)

        result.append(new_row)

    return result


size = 200

A = []
B = []

for _ in range(size):
    row = []
    for _ in range(size):
        row.append(random.randint(1, 10))
    A.append(row)

for _ in range(size):
    row = []
    for _ in range(size):
        row.append(random.randint(1, 10))
    B.append(row)


start = time.perf_counter()
python_result = matmul(A, B)
end = time.perf_counter()

python_time = end - start
print("Pure Python time:", python_time)


A_np = np.array(A)
B_np = np.array(B)

start = time.perf_counter()
numpy_result = A_np @ B_np
end = time.perf_counter()

numpy_time = end - start
print("NumPy time:", numpy_time)


speedup = python_time / numpy_time
print("Speedup:", speedup)


print("Results match:", np.array_equal(np.array(python_result), numpy_result))