
def canCompleteCircuit(A, B):
    gross = []
    n = len(A)
    for i in range(n):
        gross.append(A[i] - B[i])

    start = 0
    if sum(A) < sum(B):
        return -1

    while start < n:
        i = start
        gas = 0
        while gas >= 0:
            gas += gross[i]
            if i + 1 == n:
                i = 0
            else:
                i += 1
            if gas >= 0 and start == i:
                return start
        start += 1

    return -1


def gasStations(gas, cost):
    # TC: O(n) SP: O(1)

    if sum(cost) > sum(gas):
        return -1
    tank, start, n = 0, 0, len(gas)

    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    return start


A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 1, 2]

print(gasStations(A, B))
