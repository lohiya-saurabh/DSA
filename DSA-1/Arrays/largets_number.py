def largestNumber(A):
    B = [str(x) for x in A]
    B = sorted(B)[::-1]
    return ''.join(B)


print(largestNumber([9, 10, 4]))
