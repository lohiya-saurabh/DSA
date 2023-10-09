def platesBetweenCandles(s, queries):
    s = list(s)
    plates_count_left_to_right = [0 for _ in s]
    plates = 0
    carry_forward = 0
    for i, x in enumerate(s):
        if x == '*':
            plates += 1
            plates_count_left_to_right[i] = carry_forward
        else:
            carry_forward = plates
            plates_count_left_to_right[i] = plates
    res = []
    plates = 0
    plates_count_till_nearest_right_candle = [0 for _ in s]
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '|':
            plates = plates_count_left_to_right[i]
        plates_count_till_nearest_right_candle[i] = plates
    print(plates_count_left_to_right)
    for query in queries:
        res.append(plates_count_left_to_right[query[1]] -
                   plates_count_till_nearest_right_candle[query[0]])
    return res


print(platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]])
      )
