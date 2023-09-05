def trap(A):
    n = len(A)
    left_walls = [0]*n
    right_walls = [0]*n
    for i in range(1, len(A)):
        left_walls[i] = max(left_walls[i - 1], A[i - 1])

    for i in range(n - 2, -1, -1):
        right_walls[i] = max(right_walls[i + 1], A[i + 1])

    rain_water_trapped = 0
    for i in range(n):
        rain_water_trapped += max(min(left_walls[i], right_walls[i]) - A[i], 0)

    return rain_water_trapped


heights = [56, 6, 52, 43, 23, 47, 48, 38, 96, 46, 30, 66, 80, 15, 62, 71, 61, 12, 98, 9, 28, 81, 70, 59, 95, 34, 9, 60, 70,
           81, 71, 67, 58, 20, 22, 3, 95, 85, 20, 24, 74, 5, 23, 33, 75, 50, 38, 75, 68, 26, 46, 30, 75, 18, 4, 42, 51, 59, 8, 77]

print(trap(heights))
