class Solution:
    # @param A : list of integers
    # @return a list of integers
    def moveZeroes(self, A):
        i = j = 0
        while i < len(A):
            if A[i] != 0:
                A[j] = A[i]
                j += 1
            i += 1
        while j < len(A):
            A[j] = 0
            j += 1
        return A
