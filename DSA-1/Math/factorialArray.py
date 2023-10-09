import math


def solve(A):
    freqs = {}
    totalPrimesTillA = findAllPrimes(max(A))
    totalPrimeFactorsMap = []
    for ele in A:
        if ele <= 1:
            totalPrimeFactorsMap.append(0)
        else:
            totalPrimeFactorsMap.append(totalPrimesTillA[ele - 1])
    for i in totalPrimeFactorsMap:
        if i in freqs:
            freqs[i] += 1
        else:
            freqs[i] = 1
    totalSubsequences = 0
    for key in freqs:
        if key == 0:
            continue
        totalSubsequences += 2**freqs[key] - 1
    return totalSubsequences % (10**9 + 7)


def findAllPrimes(A):
    sqrt_A = math.sqrt(A)
    isPrime = [True for ele in range(A)]
    isPrime[0] = False
    for i in range(2, int(sqrt_A) + 1):
        for j in range(2*i, A + 1, i):
            isPrime[j - 1] = False
    total = 0
    totalPrimes = []
    for val in isPrime:
        total += 1 if val else 0
        totalPrimes.append(total)
    return totalPrimes


print(solve([12, 16, 21, 25, 27, 31, 0]))
