from nextSmallerOnLeft import nextSmallerOnLeft
from nextSmallerOnRight import nextSmallerOnRight


def largestRectangleArea(self, A):
    nsl = nextSmallerOnLeft(A)
    nsr = nextSmallerOnRight(A)
    max_area = 0
    for i in range(len(A)):
        max_area = max(max_area, (nsr[i] - nsl[i] - 1)*A[i])
    return max_area
