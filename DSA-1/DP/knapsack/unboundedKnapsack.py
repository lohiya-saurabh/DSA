def unboundedKnapsack(weights, values, bagpackCapacity):
    knapsack = [[0 for _ in range(bagpackCapacity + 1)] for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1 ):
        for j in range(1, bagpackCapacity + 1):
            if j >= weights[i - 1]:
                remaining_weight = j%weights[i - 1]
                curr_weight_mult = j//weights[i - 1]
                knapsack[i][j] = max(knapsack[i - 1][j], curr_weight_mult*values[i - 1] + knapsack[i - 1][remaining_weight])
            else:
                knapsack[i][j] = knapsack[i - 1][j]
    return knapsack[-1][-1]


print(unboundedKnapsack([1, 2, 4, 5], [22, 30, 90, 110], 10))