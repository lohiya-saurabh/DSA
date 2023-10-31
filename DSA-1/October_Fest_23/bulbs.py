k = int(input())

bulbs = '011001000101111010110'


for i in range(1, len(bulbs) + 1):
    l = i
    totalOps = 0
    j = 0
    while j < len(bulbs):
        if bulbs[j] == '1':
            j += l
            totalOps += 1
            if totalOps > k:
                break
        else:
            j += 1
    if totalOps <= k:
        print(l)
        break


