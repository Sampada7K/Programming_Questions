def rotate_matrix_clockwise(matrix):

    n = len(matrix)
    clockwise_rotated_matrix = [[0 for i in range(n)] for i in range(n)]
    print(clockwise_rotated_matrix)

    for i in range(n):
        for j in range(n):
            clockwise_rotated_matrix[j][n-1-i] = matrix[i][j]

    return clockwise_rotated_matrix


print(rotate_matrix_clockwise([[1,2,3], [4,5,6], [7,8,9]]))


def rotate_matrix_clockwise_inplace(matrix):

    n = len(matrix)

    for i in range(n//2):
        for j in range(i, n-1-i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp

    return matrix

print(rotate_matrix_clockwise_inplace([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]))

