def plusOne(A):
    num = 1
    carry = 0
    i = 0
    if len(A) > 1:
        while True and A[i] == 0:
            A.pop(0)
    for i in range(len(A) - 1, -1, -1):
        carry = (num + A[i])//10
        A[i] = (num + A[i]) % 10
        if carry == 0:
            break
    if carry != 0:
        A.insert(0, carry)
    return A


print(plusOne([0, 2, 5, 6, 8, 6, 1, 2, 4, 5]))
