from nextSmallerOnLeft import nextSmallerOnLeft
from nextSmallerOnRight import nextSmallerOnRight


def solve(A):
    rows = len(A)
    cols = len(A[0])
    histogram = [[0 for _ in range(cols)] for _ in range(rows)]
    max_area = 0

    for i in range(rows):
        curr_height = 0
        for j in range(cols):
            if A[i][j] == 1:
                curr_height += 1
            else:
                curr_height = 0
            histogram[i][j] = curr_height

    for j in range(cols):
        curr_arr = []
        for i in range(rows):
            curr_arr.append(histogram[i][j])
        nsl = nextSmallerOnLeft(curr_arr)
        nsr = nextSmallerOnRight(curr_arr)
        for i in range(len(curr_arr)):
            max_area = max(max_area, (nsr[i] - nsl[i] - 1)*curr_arr[i])

    return max_area


# Test Case
A = [[0, 1, 1], [1, 0, 0], [1, 0, 0], [
    1, 0, 0], [1, 0, 0], [1, 1, 1], [0, 1, 0]]
print(solve(A))
