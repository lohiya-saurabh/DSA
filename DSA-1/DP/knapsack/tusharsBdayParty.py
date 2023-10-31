from random import randint

def calculateMinCostToFill(eatingCapacity, fillingCapacity, costOfDishes):
    costAndCapacity = sorted(zip(costOfDishes, fillingCapacity), key=lambda x: x[1])
    minCostToFill = [[j*costAndCapacity[0][0] for j in range(max(eatingCapacity)+1)] for _ in range(len(fillingCapacity)+1)]
    for i in range(1, len(minCostToFill)):
        for j in range(1, max(eatingCapacity)+1):
            if j >= costAndCapacity[i - 1][1]:
                minCostToFill[i][j] = min(minCostToFill[i - 1][j], costAndCapacity[i - 1][0] + minCostToFill[i][j- costAndCapacity[i - 1][1]])
            else:
                minCostToFill[i][j] = minCostToFill[i - 1][j]
    minCost = 0
    for j in eatingCapacity:
        minCost += minCostToFill[-1][j]
    return minCost




def arrayGenerator(arrLen, maxNum, fillWithOnes=False):
    arr = [randint(1, maxNum) for _ in range(arrLen)]
    if fillWithOnes:
        return arr if 1 in arr else arrayGenerator(arrLen, maxNum, True)
    else:
        return arr
        
        

noOfTestcases = 100

    
def minCost(A, B, C):
    dp = [[0 for i in range(1005)] for j in range(1005)]
    dish = []
    n = len(C)
    for i in range(n):
        dish.append([B[i], C[i]])
    m = max(A)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = float("inf")
            else:
                if i >= dish[j - 1][0]:
                    dp[i][j] = min(
                        dp[i][j - 1], dp[i - dish[j - 1][0]][j] + dish[j - 1][1]
                    )
                else:
                    dp[i][j] = dp[i][j - 1]
    ans = 0
    for i in range(len(A)):
        ans += dp[A[i]][n]
    return ans

# print(minCostToFillTummies([2,3,1,5,4], [3,2,4,1], [1,2,5,10]))
# print(minCostToFillTummies([10], [1, 2, 6], [10, 2, 4]))


for _ in range(noOfTestcases):
    eatingCapacities = arrayGenerator(5, 10)
    fillingCapacities = arrayGenerator(4, 7, True)
    costOfDishes = arrayGenerator(4, 10)
    ans1 = calculateMinCostToFill(eatingCapacities, fillingCapacities, costOfDishes)
    ans2 = minCost(eatingCapacities, fillingCapacities, costOfDishes)
    print(eatingCapacities, fillingCapacities, costOfDishes)
    print(ans1, ans2)
    if ans1 == ans2:
        print("Testcase passed")
    else:
        print("Testcase failed")


print(calculateMinCostToFill([5, 9, 2, 10, 9], [1, 4, 3, 4], [4, 1, 3, 6]))
# print(minCost([1, 5, 8, 5, 3], [7, 6, 6, 1], [6, 3, 4, 6]))