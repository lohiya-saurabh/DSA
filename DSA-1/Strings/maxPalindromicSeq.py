class Solution:
    def getMaxPalindromicSeq(self, i, j, seq, s):
        maxLen = len(seq)
        while i > -1 and j < len(s):
            if s[i] == s[j]:
                if j - i + 1 > maxLen:
                    maxLen = j - i - 1
                    seq = s[i:j + 1]
                i -= 1
                j += 1
            else:
                break
        return seq

    def longestPalindrome(self, s: str) -> str:
        i = 0
        palSeq = s[0]
        while i < len(s):
            if i - 1 > -1 and i + 1 < len(s) and s[i + 1] == s[i - 1]:
                palSeq = self.getMaxPalindromicSeq(i - 1, i + 1, palSeq, s)
            if i + 1 < len(s) and s[i] == s[i + 1]:
                palSeq = self.getMaxPalindromicSeq(i, i + 1, palSeq, s)
            i += 1
        return palSeq


x = Solution()

print(x.longestPalindrome('aaaa'))
