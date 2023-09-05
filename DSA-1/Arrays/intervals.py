# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def insert(intervals, new_interval):
    new_intervals = []
    i = 0
    flag = False
    while i < len(intervals):
        interval = intervals[i]
        if interval[1] >= new_interval[0] and interval[0] <= new_interval[1]:
            new_interval[0] = min(interval[0], new_interval[0])
            new_interval[1] = max(interval[1], new_interval[1])
        else:
            if not flag and interval[0] > new_interval[1]:
                new_intervals.append(new_interval)
                flag = True
            new_intervals.append(interval)
        i += 1
    if not flag:
        new_intervals.append(new_interval)
        flag = True
    return new_intervals


def disjointIntervals(A):
    i = 0
    j = 1
    ans = set()
    if len(A) <= 1:
        return len(A)
    A = sorted(A, key=lambda x: x[0])
    while j < len(A):
        prev_interval = A[i]
        curr_interval = A[j]
        if prev_interval[1] >= curr_interval[0]:
            if prev_interval[1] <= curr_interval[1]:
                ans.add(i)
            else:
                ans.discard(i)
                ans.add(j)
                i = j
        else:
            ans.add(i)
            ans.add(j)
            i = j
        j += 1
    return len(ans)


def totalMeetingRooms(meetings):
    i = 0
    j = 1
    curr_rooms_req = 1
    max_rooms_req = 1
    if len(meetings) <= 1:
        return len(meetings)
    meetings = sorted(meetings, key=lambda x: x[0])
    while j < len(meetings):
        prev_meeting = meetings[i]
        curr_meeting = meetings[j]
        if prev_meeting[1] > curr_meeting[0]:
            if prev_meeting[1] > curr_meeting[1]:
                i = j
            curr_rooms_req += 1
        else:
            i = j
            max_rooms_req = max(max_rooms_req, curr_rooms_req)
            curr_rooms_req = 1
        j += 1
    return max_rooms_req


def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    last_interval = intervals[0]
    merged_intervals = []
    for interval in intervals[1:]:
        if interval[0] > last_interval[1]:
            merged_intervals.append(last_interval)
            last_interval = interval
        else:
            last_interval[1] = max(last_interval[1], interval[1])
    merged_intervals.append(last_interval)
    return merged_intervals

# intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# newInterval = [4, 9]


# print(insert(intervals, newInterval))
A = [[0, 14], [6, 25], [12, 19], [13, 19], [5, 9]]

intervals = [[3, 13], [7, 7], [3, 10], [4, 8], [7, 8], [9, 12], [3, 6], [7, 12], [4, 10], [3, 8], [5, 11], [9, 10], [3, 7], [4, 4], [7, 15], [2, 9],
             ]
print(totalMeetingRooms(A))
