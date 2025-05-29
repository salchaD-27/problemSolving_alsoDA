# import bisect
# class MyCalendarTwo:
#     def __init__(self): self.arr=[]
#     def book(self, startTime: int, endTime: int) -> bool:
#         flag=0
#         i = bisect.bisect_right(self.arr, (startTime, endTime))
#         if i > 0 and self.arr[i - 1][1] > startTime: flag+=1
#         if i < len(self.arr) and self.arr[i][0] < endTime: flag+=1
#         if flag>2: return False
#         self.arr.insert(i, (startTime, endTime)) 
#         return True

class MyCalendarTwo:
    def __init__(self):
        self.booked = []
        self.overlaps = []
    def book(self, start: int, end: int) -> bool:
        for os, oe in self.overlaps:
            if start < oe and end > os: return False
        for bs, be in self.booked:
            if start < be and end > bs: self.overlaps.append((max(start, bs), min(end, be)))
        self.booked.append((start, end))
        return True