# def convert(A, B):
#     n = len(A)
#     zigzagStr = ""
#     i = 0
#     while i < B:
#         flag = True
#         j = i
#         while j < n:
#             zigzagStr += A[j]
#             if B == 1:
#                 j += 1
#             elif i % (B - 1) == 0:
#                 j += (B - 1)*2
#             elif flag and i != B - 1:
#                 j += (B - 1 - i)*2
#             elif not flag and i != B - 1:
#                 j += i*2
#             flag = not flag
#         i += 1
#     return zigzagStr


def convert(A, B):
    n = len(A)
    count = 0
    zigzagA = []
    rowsRead = 0
    row = 0
    if B == 1:
        return A
    downInc = (B - 1)*2 - rowsRead*2
    upInc = 0
    while count < n:
        direction = "down"
        i = row
        while i < n:
            zigzagA.append(A[i])
            if row == 0:
                i += downInc
            elif row == B - 1:
                i += upInc
            elif direction == "down":
                i += downInc
                direction = "up"
            else:
                direction = "down"
                i += upInc
            count += 1
        upInc += 2
        downInc -= 2
        row += 1
    return "".join(zigzagA)


print(convert("A", 1))
