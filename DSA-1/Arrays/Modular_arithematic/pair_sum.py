def solve(A, B):
    A = [ele % B for ele in A]
    A_hash = {}
    count = 0
    for ele in A:
        if ele in A_hash:
            A_hash[ele] += 1
        else:
            A_hash[ele] = 1

    for ele in A_hash:
        if ele == B - ele or ele == 0:
            count += (A_hash[ele] * (A_hash[ele] - 1)) // 2
            A_hash[ele] = 0
        elif B - ele in A_hash:
            count += A_hash[ele] * A_hash[B - ele]
            A_hash[ele] = 0
            A_hash[B - ele] = 0
    return count % (10**9 + 7)


print(solve([1, 2, 3, 4, 5], 2))
