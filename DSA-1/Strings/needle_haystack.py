def needleAndHaystack(haystack: str, needle: str) -> int:
    i = 0
    j = 0
    while j < len(haystack):
        if haystack[j] == needle[i]:
            i += 1
            j += 1
        else:
            i = 0
            j = j - i + 2
        if i == len(needle):
            return j - len(needle)
    return -1


haystack = "mississippi"
needle = "issi"

print(needleAndHaystack(haystack, needle))
