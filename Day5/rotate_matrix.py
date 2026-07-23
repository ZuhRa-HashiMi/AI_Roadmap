def rotate_90_clockwise(matrix):
    n = len(matrix)

    # Step 1: transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: reverse each row
    for row in matrix:
        row.reverse()

    return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = rotate_90_clockwise(matrix)

for row in rotated:
    print(row)