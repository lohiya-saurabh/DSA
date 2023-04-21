def maxProfit(A):
    purchasePrice = float('inf')
    totalProfit = 0
    stockPrice = 0
    for stockPrice in A:
        if stockPrice > purchasePrice:
            totalProfit += stockPrice - purchasePrice
        purchasePrice = stockPrice
    return totalProfit
