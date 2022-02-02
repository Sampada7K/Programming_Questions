def rec_bounded_knapsack(weights, values, w, n):
    if n == 0 or w == 0:
        return 0

    if weights[n-1] > w:
        return rec_bounded_knapsack(weights, values, w, n-1)
    else:
        return max(rec_bounded_knapsack(weights, values, w, n-1),
                   values[n-1] + rec_bounded_knapsack(weights, values, w-weights[n-1], n-1))


values1 = [60, 100, 120]
weights1 = [10, 20, 30]
w1 = 60
n1 = len(values1)

print(rec_bounded_knapsack(weights1, values1, w1, n1))


def dp_bounded_knapsack(weights, values, w, n):
    dp_array = [[-1 for j in range(w+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                dp_array[i][j] = 0
            elif weights[i-1] <= j:
                dp_array[i][j] = max(dp_array[i-1][j], values[i-1]+dp_array[i-1][j-weights[i-1]])
            else:
                dp_array[i][j] = dp_array[i-1][j]
    for row in dp_array:
        print(row)
    return dp_array[n][w]


print(dp_bounded_knapsack(weights1, values1, w1, n1))






