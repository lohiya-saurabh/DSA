def power(A):
    bin_A = bin(int(A))
    for i in range(3, len(bin_A)):
        if bin_A[i] != 0:
            return 0
    return 1


print(power("22"))
