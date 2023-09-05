def pascalTriangle(N):
    res = []
    for i in range(N):
        curr_row = [1]
        curr = 1
        prev = 1
        for j in range(1, i + 1):
            curr = prev*(i - j + 1)//j
            prev = curr
            curr_row.append(curr)
        res.append(curr_row)
    return res


print(pascalTriangle(6))
