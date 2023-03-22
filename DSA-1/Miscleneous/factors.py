def factors(n):
    ans = 0
    for i in range(n//2 + 1):
        if n//i == 0:
            ans += 1
    return ans
