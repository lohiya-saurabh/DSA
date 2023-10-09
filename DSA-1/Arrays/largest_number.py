def largestNumber(A):
    strA = [str(x) for x in A]
    strA.sort()
    strA.reverse()
    final = ""
    i = 0
    print(strA)
    while i < len(A):
        num1 = int(final + strA[i])
        num2 = int(strA[i] + final)
        if num1 > num2:
            final = final + strA[i]
        else:
            final = strA[i] + final
        i += 1
    return int(final)


print(largestNumber([3, 30, 34, 5, 9]))