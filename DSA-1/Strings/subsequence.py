
def canMakeSubsequence(str1, str2):
    if len(str1) < len(str2):
        return False
    str1 = list(str1)
    str2 = list(str2)
    updated_str1, updated_str2 = new_str(str1, str2)
    for i in range(len(updated_str2)):
        updated_str2[i] = chr(97 + (ord(updated_str2[i]) - 98) % 26)
    return isSubsequence("".join(updated_str1), "".join(updated_str2))


def new_str(str1, str2):
    str2_hash = {}
    for char in str2:
        if char in str2_hash:
            str2_hash[char] += 1
        else:
            str2_hash[char] = 1
    updated_str1 = []
    i = 0
    while i < len(str1):
        if str1[i] in str2_hash:
            if str2_hash[str1[i]] > 1:
                str2_hash[str1[i]] -= 1
            else:
                del str2_hash[str1[i]]
        else:
            updated_str1.append(str1[i])
        i += 1
    j = 0
    updated_str2 = []
    while j < len(str2):
        if str2[j] in str2_hash:
            if str2_hash[str2[j]] > 1:
                str2_hash[str2[j]] -= 1
            else:
                del str2_hash[str2[j]]
            updated_str2.append(str2[j])
        j += 1

    return [updated_str1, updated_str2]


def isSubsequence(str1, str2):
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            j += 1
        i += 1
    return j == len(str2)


print(canMakeSubsequence("eao", "ofa"))
