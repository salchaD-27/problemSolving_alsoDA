# class MyCalendar:
#     def __init__(self): self.bookings=[]
#     def book(self, startTime: int, endTime: int) -> bool:
#         for booking in self.bookings:
#             start,end=booking[0],booking[1]
#             if startTime<start and start<endTime<=end: return False
#             elif start<=startTime<=end and start<=endTime<=end: return False
#             elif startTime<=start and end<endTime: return False
#             elif start<=startTime<=end and end<=endTime: return False
#             else: self.bookings.append([startTime, endTime])
#         return True

# class MyCalendar:
#     def __init__(self): self.bookings = []
#     def book(self, startTime: int, endTime: int) -> bool:
#         for start, end in self.bookings:
#             if not (endTime <= start or end <= startTime): return False
#         self.bookings.append([startTime, endTime])
#         return True

import bisect
class MyCalendar:
    def __init__(self): self.arr=[]
    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect.bisect_right(self.arr, (startTime, endTime))
        if i > 0 and self.arr[i - 1][1] > startTime: return False
        if i < len(self.arr) and self.arr[i][0] < endTime: return False
        self.arr.insert(i, (startTime, endTime)) 
        return True