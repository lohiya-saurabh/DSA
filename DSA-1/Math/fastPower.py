def fastPowerModN(a, b, n):
    res = 1
    while b > 0:
        if b & 1 == 1:
            res = (res * a) % n
        a = (a * a) % n
        b = b >> 1
    return res


print(fastPowerModN(5, 2, 16))
