def transpose(A):
    rows = len(A)
    cols = len(A[0])

    result = []

    for col in range(cols):
        new_row = []

        for row in range(rows):
            new_row.append(A[row][col])

        result.append(new_row)

    return result


def matvec(A, v):
    result = []

    for row in A:
        total = 0

        for i in range(len(v)):
            total += row[i] * v[i]

        result.append(total)

    return result


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


A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

v = [5, 6]

print("Transpose of A:")
print(transpose(A))

print("A multiplied by vector v:")
print(matvec(A, v))

print("A multiplied by B:")
print(matmul(A, B))