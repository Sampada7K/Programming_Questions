def zero_matrix(matrix):
    # rows
    m = len(matrix)
    # columns
    n = len(matrix[0])

    zero_positions = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_positions.append((i, j))
    print(zero_positions)
    if len(zero_positions) != 0:
        for index_values in zero_positions:
            for col in range(n):
                matrix[index_values[0]][col] = 0
            for row in range(m):
                matrix[row][index_values[1]] = 0

    return matrix


# print(zero_matrix([[1, 0, 3], [4, 5, 6]]))
# print(zero_matrix([[1, 4], [0, 5], [3, 6]]))
# print(zero_matrix([[1, 2, 3], [4, 5, 6], [0, 8, 9]]))
# print(zero_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(zero_matrix([[1, 2, 3, 0], [4, 0, 5, 6], [7, 8, 9, 10]]))
