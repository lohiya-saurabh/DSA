def restoreIPAddresses(ipString):
    result = []
    segments = []
    start = 0
    n = len(ipString)
    if n > 12:
        return result
    backtrack(ipString, start, segments, result)
    return result


def backtrack(s, start, segments, result):
    n = len(s)

    if len(segments) == 4 and start == n:
        result.append(".".join(segments))
        return

    if len(segments) == 4:
        return

    for i in range(start, min(start + 3, n)):
        if isValidIpSegment(s[start: i + 1]):
            tempSegment = segments.copy()
            tempSegment.append(s[start: i + 1])
            backtrack(s, i + 1, tempSegment, result)


def isValidIpSegment(ipSegment):
    if int(ipSegment) >= 256 or (len(ipSegment) > 1 and ipSegment[0] == "0"):
        return False
    return True


print(restoreIPAddresses("25525511135"))
