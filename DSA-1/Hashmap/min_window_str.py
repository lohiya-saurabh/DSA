

# Given a string A and a string B, find the window with minimum length in A,
# which will contain all the characters in B in linear time complexity.
# Note that when the count of a character c in B is x, then the count of c
# in the minimum window in A should be at least x.

def minWindowStr(A, B):
    map_b = {}
    map_window_string = {}
    stack = []
    res = ""
    for char in B:
        if char in map_b:
            map_b[char] += 1
        else:
            map_b[char] = 1

    min_window_size = float('inf')
    visited = set()

    for i in range(len(A)):
        char = A[i]
        if char in map_b:
            if char in map_window_string:
                map_window_string[char] += 1
                while len(stack) > 0 and map_window_string[A[stack[0]]] > map_b[A[stack[0]]]:
                    map_window_string[A[stack.pop(0)]] -= 1
            else:
                map_window_string[char] = 1
            if map_window_string[char] == map_b[char]:
                visited.add(char)

            stack.append(i)
            if len(visited) == len(map_b):
                if stack[-1] - stack[0] + 1 < min_window_size:
                    min_window_size = stack[-1] - stack[0] + 1
                    res = A[stack[0]: stack[-1] + 1]
    return res
