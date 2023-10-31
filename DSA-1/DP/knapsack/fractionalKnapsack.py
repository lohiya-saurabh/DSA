def fractionalKnapsack(weights, values, bagpackCapacity):
    values_per_weight = [[values[i]/weights[i], weights[i]] for i in range(len(weights))]
    values_per_weight = sorted(values_per_weight , key = lambda x: x[0], reverse = True)
    curr_weight = 0
    curr_value = 0
    for i in range(len(values_per_weight)):
        if curr_weight + values_per_weight[i][1] <= bagpackCapacity:
            curr_weight += values_per_weight[i][1]
            curr_value += values_per_weight[i][0]*values_per_weight[i][1]
        else:
            remaining_weight = bagpackCapacity - curr_weight
            curr_value += values_per_weight[i][0]*remaining_weight
            break
    print(values_per_weight)
    return "{:.2f}".format(curr_value*100)


print(fractionalKnapsack([20], [3], 17))