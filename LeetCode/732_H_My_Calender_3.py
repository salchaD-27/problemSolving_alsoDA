from collections import defaultdict
class MyCalendarThree:
    def __init__(self):
        self.timeline = defaultdict(int)
        self.max_k = 0
    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1
        curr = 0
        for time in sorted(self.timeline):
            curr += self.timeline[time]
            self.max_k = max(self.max_k, curr)
        return self.max_k