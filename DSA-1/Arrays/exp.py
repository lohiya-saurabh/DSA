# arr = [1, 2, 3, 4, 5]

# print(filter(lambda x: x % 2 == 0, arr))[0]
# print(arr.find(lambda x: x % 2 == 0))
# print(next(x for x in arr if x % 2 == 0))


# 2 3 1 0

# 1 0 3 2
# 4 5 5 4 1
# 5 8
def sort(arr=[3, 30, 34, 5, 9]):
    arr = [str(x) for x in arr]
    sortArr = sorted(arr)[:: -1]
    final = ""
    for i in range(len(arr) - 1):
        if sortArr[i]*10**len(str(sortArr[i + 1])) + sortArr[i + 1] > sortArr[i + 1]*10**len(str(sortArr[i])) + sortArr[i]:
            final += str(sortArr[i])
        else:
            final += str(sortArr[i + 1])
    return final


print(sort())
