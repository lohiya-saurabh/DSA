import re


def isPalindrome(A):
    A = re.sub(r'[^a-zA-Z0-9]|\s', "", A)
    return checkPalindrome(A)


def checkPalindrome(A):
    start = 0
    end = len(A) - 1
    A = A.lower()
    while start < end:
        if A[start] != A[end]:
            return 0
        start += 1
        end -= 1
    return 1

# Write a Function to identify minimum number of characters
# required to make string palindromic where only characters can
# be added in front


def max_chars_required(str):
    stack = []
    max_pal_len = 0
    for i in range(len(str)):
        max_pal_len = max(max_pal_len, checkPalindrome(str[:i + 1]))
    return len(str) - max_pal_len


print(isPalindrome("A man, a plan, a canal: Panama#"))
