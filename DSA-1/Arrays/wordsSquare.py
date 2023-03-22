
def validWordSquare(words):
    i = 0
    j = 0
    for i in range(len(words)):
        words[i] = list(words[i])
        if len(words[i]) != len(words):
            words[i] += ["_"] * (len(words) - len(words[i]))
    for i in range(len(words)):
        for j in range(i + 1, len(words[i])):
            if words[i][j] != words[j][i]:
                return False
    return True


print(validWordSquare(["abcd", "bnrt", "crm", "dt"]))
