def buyingCandies(candies, sweetness, costs, money):
    maxSweetness = [[0 for i in range(money + 1)] for _ in range(len(candies) + 1)]
    for i in range(1, len(candies) + 1):
        for j in range(1, money + 1):
            if j//costs[i - 1] >= 1:
                maxSweetness[i][j] = max(maxSweetness[i- 1][j], candies[i - 1]*sweetness[i - 1] + maxSweetness[i - 1][j - costs[i - 1]])
            else:
                maxSweetness[i][j] = maxSweetness[i - 1][j]
    return maxSweetness[-1][-1]



print(buyingCandies([1, 2, 3], [2,2,10], [2,3,9], 8))