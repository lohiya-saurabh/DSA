import math


def solve(A):
    sqrt_A = math.sqrt(A)
    isPrime = [True for ele in range(A)]
    isPrime[0] = False
    for i in range(2, int(sqrt_A) + 1):
        for j in range(2*i, A + 1, i):
            isPrime[j - 1] = False
    total = 0
    for val in isPrime:
        total += 1 if val else 0
    return total


print(solve(10))
