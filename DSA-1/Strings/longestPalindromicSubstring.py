class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        longest_palindrome = ""
        longest_palindrome_len = 0
        n = len(A)
        for i in range(n):
            [odd_palindrome, odd_len] = self.checkPalindrome(A, i - 1, i + 1)
            [even_palindrome, even_len] = self.checkPalindrome(A, i, i + 1)
            if odd_len > even_len:
                if odd_len > longest_palindrome_len:
                    longest_palindrome = odd_palindrome
                    longest_palindrome_len = odd_len
            else:
                if even_len > longest_palindrome_len:
                    longest_palindrome = even_palindrome
                    longest_palindrome_len = even_len

        return longest_palindrome

    def checkPalindrome(self, A, left, right):
        start = 0
        end = len(A) - 1
        while start <= left and end >= right:
            if A[left] == A[right]:
                left -= 1
                right += 1
            else:
                break
        curr_palindrome = A[left: right + 1]
        curr_palindrome_len = len(A[left: right + 1])
        return [curr_palindrome, curr_palindrome_len]
