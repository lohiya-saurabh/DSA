def knapsack(weights, values, bagCapacity):
    matrix = [[0 for _ in range(bagCapacity + 1)] for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for j in range(1, bagCapacity + 1):
            if weights[i - 1] <= j:
                matrix[i][j] = max(matrix[i - 1][j], values[i - 1] + matrix[i - 1][j - weights[i - 1]])
            else:
                matrix[i][j] = matrix[i - 1][j]
    return matrix[-1][-1]
