def solve(A):
    result = 0
    for num in A:
        result ^= num
    i = 0
    while result & 1 != 1:
        result >>= 1
        i += 1
    grp1 = 0
    grp2 = 0
    for num in A:
        if num & (1 << i) != 0:
            grp1 = grp1 ^ num
        else:
            grp2 = grp2 ^ num
    return [grp1, grp2] if grp1 < grp2 else [grp2, grp1]


def binary(num):
    return bin(num)[2:]


arr = [186, 256, 102, 377, 186, 377]

for num in arr:
    print(binary(num))


print(solve(arr))
