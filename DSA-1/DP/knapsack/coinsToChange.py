def coinchange2(A, B):
    noOfWays = [0 for _ in range(B + 1)]
    noOfWays[0] = 1
    A.sort()
    for i in range(len(A)):
        for j in range(1, B + 1):
            if j >= A[i]:
                noOfWays[j] = noOfWays[j] + noOfWays[j - A[i]]
    return noOfWays[-1]