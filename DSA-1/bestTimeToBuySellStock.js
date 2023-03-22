function maxProfit(prices) {
  let minPrice = prices[0]
  let maxProfit = 0
  for (let i = 1; i < prices.length; i++) {
    maxProfit = Math.max(prices[i] - minPrice, maxProfit)
    minPrice = Math.min(minPrice, prices[i])
  }
  return maxProfit
};