"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        last = 0
        intervals = sorted(intervals, key = lambda x : x.start)
        for interval in intervals:
            if interval.start < last:
                return False
            last = interval.end
        return True