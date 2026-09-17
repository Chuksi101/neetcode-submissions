class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        '''
        intervals.sort(key = lambda x: x[0])
        prevEnd = intervals[0][1]
        res = 0

        for i in intervals[1:]:
            if i[0] < prevEnd:
                res += 1
                prevEnd = min(prevEnd, i[1])
            else:
                prevEnd = i[1]

        return res
