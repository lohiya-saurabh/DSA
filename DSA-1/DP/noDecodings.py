def numDecodings(A):
    # Approach 1: Recursion
    # return numDecodingsHelper(A)

    # Approach 2: DP
    noOfWays = [0 for _ in range(len(A))]
    A = [int(i) for i in A]
    if A[0] != 0:
        noOfWays[0] = 1
    for i in range(1, len(A)):
        if A[i] != 0:
            noOfWays[i] = noOfWays[i - 1]
        if A[i-1]*10 + A[i] >= 10 and A[i-1]*10 + A[i] <= 26:
            if i == 1:
                noOfWays[i] += 1
            else:
                noOfWays[i] += noOfWays[i - 2]
    return noOfWays[len(A) - 1] % 1000000007


def numDecodingsHelper(A):
    curr1, curr2 = 0, 0
    if A == "":
        return 1
    if 0 < int(A[0]) < 10:
        curr1 = numDecodingsHelper(A[1:])
    if len(A) > 1 and 0 < int(A[0] + A[1]) < 27 and A[0] != '0':
        curr2 = numDecodingsHelper(A[2:])
    return curr1 + curr2


print(numDecodings("12012"))
