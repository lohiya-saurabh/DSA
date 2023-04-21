def longestIncreasingSubsequence(stockPrices):
    currStreak = 0
    longestStreak = 0
    prevStockPrice = float('-inf')
    noOfTradingDays = len(stockPrices)
    for i in range(noOfTradingDays):
        if stockPrices[i] > prevStockPrice:
            currStreak += 1
        else:
            currStreak = 1
        prevStockPrice = stockPrices[i]
        longestStreak = max(longestStreak, currStreak)
    return longestStreak


print(longestIncreasingSubsequence(
    [12, 3, 15, 8, 12, 16, 5, 3, 9, 10, 19, 27, 28, 29, 30, 16]))
