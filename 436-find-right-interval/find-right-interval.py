class Solution(object):
    def findRightInterval(self, intervals):
        n = len(intervals)
        starts = sorted((intervals[i][0], i) for i in range(n))
        starts_only = [s[0] for s in starts]
        result = [-1] * n

        for i in range(n):
            end = intervals[i][1]
            pos = bisect.bisect_left(starts_only, end)
            if pos < n:
                result[i] = starts[pos][1]

        return result