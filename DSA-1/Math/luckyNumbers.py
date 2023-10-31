import math


def solve(A):
    allPrimes = findAllPrimes(A)
    primes = []
    for i, val in enumerate(allPrimes):
        if val:
            primes.append(i + 1)
    i, n = 0, len(primes)
    countLuckyNumbers = 0
    totalPrimesTillA = totalPrimesTill(A)
    while i < n:
        j = n - 1
        while j > i:
            currMul = primes[i]*primes[j]
            if currMul <= A:
                # total primes)
                tmp = totalPrimesTillA[A//currMul]
                if tmp >= 2:
                    countLuckyNumbers += A//currMul - tmp + 2
                else:
                    countLuckyNumbers += 1
            j -= 1
        i += 1
    return countLuckyNumbers


def findAllPrimes(A):
    sqrt_A = math.sqrt(A)
    isPrime = [True for ele in range(A)]
    isPrime[0] = False
    for i in range(2, int(sqrt_A) + 1):
        for j in range(2*i, A + 1, i):
            isPrime[j - 1] = False
    return isPrime


def totalPrimesTill(A):
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


print(solve(40))
