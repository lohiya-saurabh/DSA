class Solution:
    def solve(self, A):
        # To count all 1's in the string
        cnt_one = 0
        n = len(A)
        for x in A:
            if x=='1':
                cnt_one+=1
        # To store cumulative 1's
        left = [0]*n
        right = [0]*n
        if A[0]=='1':
            left[0] = 1
        if A[n-1]=='1':
            right[n-1] = 1
        for i in range(1, n):
            if A[i]=='1':
                left[i] = left[i-1] + 1
        for i in range(n-2, -1, -1):
            if A[i]=='1':
                right[i] = right[i + 1] + 1
        cnt = 0
        max_cnt = 0;
        for i in range(n):
            max_cnt = max(max_cnt, max(right[i], left[i]))
        for i in range(1, n-1):
            if A[i]=='0':
                su = left[i-1] + right[i+1]
                cnt = su
                if su < cnt_one:
                    cnt += 1
                max_cnt = max(max_cnt, cnt);
                cnt = 0
        return max_cnt