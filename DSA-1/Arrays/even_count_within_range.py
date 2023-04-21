

def even_count_within_range(arr, queries):
    evenCountArr = [0] * len(arr)
    evenCountWithinRange = []
    for i in range(len(arr)):
        if arr[i] & 1 == 0:
            evenCountArr[i] += evenCountArr[i - 1] + 1 if i > 0 else 1
        else:
            evenCountArr[i] = evenCountArr[i - 1] if i > 0 else 0
    for query in queries:
        if query[0] > 0:
            evenCountWithinRange.append(
                evenCountArr[query[1]] - evenCountArr[query[0] - 1])
        else:
            evenCountWithinRange.append(evenCountArr[query[1]])
    return evenCountWithinRange


print(even_count_within_range([6, 3, 3, 6, 7, 8, 7, 3, 7],
                              [[2, 6], [4, 7], [6, 7]]))
