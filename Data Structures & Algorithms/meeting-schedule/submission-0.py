"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def print_intervals(intervals: list[Interval]):
    for interval in intervals:
        print(f"({interval.start},{interval.end})")


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        print_intervals(intervals)
        intervals.sort(key=lambda x: x.start)
       
        for i in range(1, len(intervals)):
            prev_interval = intervals[i-1]
            interval = intervals[i]
            if prev_interval.end > interval.start:
                return False
        return True 

