
def partitionLabels(s: str):
    lastIndex = {}
    for i in range(len(s)):
        lastIndex[s[i]] = i
    parts = []
    i = -1
    while i < len(s) - 1:
        j = i + 1
        maxIndex = lastIndex[s[j]]
        while j < maxIndex:
            maxIndex = max(maxIndex, lastIndex[s[j]])
            j += 1
        parts.append(j - i)
        i = j
    return parts


print(partitionLabels('abcaddefdss'))
