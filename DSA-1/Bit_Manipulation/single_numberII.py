def singleNumber(A):
    bit_count = [0 for _ in range(32)]
    for i in range(32):
        for j in range(len(A)):
            if A[j] & (1 << i) != 0:
                bit_count[31-i] += 1
    res = [0 for _ in range(32)]
    for i in range(32):
        if bit_count[i] % 3 == 1:
            res[i] = '1'
        else:
            res[i] = '0'
    return int("".join(res), 2)


print(singleNumber([1, 2, 5, 3, 3, 2, 2, 3, 1, 1]))
