
def seats(A):
    window_size = 0
    xPos = []
    for i, ele in enumerate(A):
        if ele == "x":
            xPos.append(i)
    if window_size == 0:
        return 0
    window_size = len(xPos)
    medianPos = xPos[window_size//2] if window_size &1 == 1 else xPos[window_size//2 - 1]
    if window_size & 1 == 1:
        windowStart = medianPos - (window_size//2)
    else:
        windowStart = medianPos - (window_size//2 - 1)
    res = 0
    for pos in xPos:
        res += abs(pos - windowStart)
        windowStart += 1
    return res

print(seats("....x..xx...x.."))