from typing import List
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        roomCount = [0] * n
        roomAvailableTime = [0] * n
        for start, end in meetings:
            duration = end - start
            assigned = False
            for i in range(n):
                if roomAvailableTime[i] <= start:
                    roomAvailableTime[i] = end
                    roomCount[i] += 1
                    assigned = True
                    break
            if not assigned:
                earliest_time = float('inf')
                chosen_room = -1
                for i in range(n):
                    if roomAvailableTime[i] < earliest_time:
                        earliest_time = roomAvailableTime[i]
                        chosen_room = i
                roomAvailableTime[chosen_room] += duration
                roomCount[chosen_room] += 1
        max_meetings = max(roomCount)
        for i in range(n):
            if roomCount[i] == max_meetings: return i

import heapq
from typing import List
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        ongoing_meetings = []
        room_meeting_count = [0] * n
        for start, end in meetings:
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                ended_time, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room)
            duration = end - start
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
                room_meeting_count[room] += 1
            else:
                end_time, room = heapq.heappop(ongoing_meetings)
                new_end = end_time + duration
                heapq.heappush(ongoing_meetings, (new_end, room))
                room_meeting_count[room] += 1
        max_meetings = max(room_meeting_count)
        for i in range(n):
            if room_meeting_count[i] == max_meetings: return i