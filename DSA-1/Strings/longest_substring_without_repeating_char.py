def longestSubstringWithoutRepeatingChars(s):
    i, j = 0, 0
    s_map = {}
    max_substring_length = 0
    while j < len(s):
        if s[j] in s_map and s_map[s[j]] >= i:
            i = s_map[s[j]] + 1
        s_map[s[j]] = j
        max_substring_length = max(max_substring_length, j - i + 1)
        j += 1

    return max_substring_length


s = "abba"
print(longestSubstringWithoutRepeatingChars(s))
