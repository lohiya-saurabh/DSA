from nextGreaterOnLeft import nextGreaterOnLeft
from nextGreaterOnRight import nextGreaterOnRight
from nextSmallerOnLeft import nextSmallerOnLeft
from nextSmallerOnRight import nextSmallerOnRight


def maxMin(arr):
    nsl = nextSmallerOnLeft(arr)
    nsr = nextSmallerOnRight(arr)
    ngl = nextGreaterOnLeft(arr)
    ngr = nextGreaterOnRight(arr)
    sum_of_subarray_values = 0
    for i in range(len(arr)):
        sum_of_subarray_values -= arr[i] * (i - nsl[i]) * (nsr[i] - i)
        sum_of_subarray_values += arr[i] * (i - ngl[i]) * (ngr[i] - i)
    return sum_of_subarray_values


print(maxMin([4, 7, 3, 8]))
