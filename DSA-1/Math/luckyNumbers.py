import math


def solve(A):
    allPrimes = findAllPrimes(A)
    primes = []
    for i, val in enumerate(allPrimes):
        if val:
            primes.append(i + 1)
    i, j = 0, len(primes) - 1
    countLuckyNumbers = 0
    while i <= j:
        primeMul = primes[i]*primes[j]
        if primeMul <= A:
            countLuckyNumbers += j - i
            i += 1
            j -= 1
        elif primeMul < A:
            i += 1
        else:
            j -= 1
    return countLuckyNumbers


def findAllPrimes(A):
    sqrt_A = math.sqrt(A)
    isPrime = [True for ele in range(A)]
    isPrime[0] = False
    for i in range(2, int(sqrt_A) + 1):
        for j in range(2*i, A + 1, i):
            isPrime[j - 1] = False
    return isPrime


print(solve(60))
