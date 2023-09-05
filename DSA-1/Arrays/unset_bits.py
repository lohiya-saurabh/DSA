def unset_bits(A, B, C):
    binary = list('{0:b}'.format(int(A)))
    n = len(binary)
    start = max(n - C, 0)
    end = n - B
    for i in range(start, end):
        if binary[i] == '1':
            binary[i] = '0'
    return int("".join(binary), 2)


print(unset_bits(15, 3, 5))
