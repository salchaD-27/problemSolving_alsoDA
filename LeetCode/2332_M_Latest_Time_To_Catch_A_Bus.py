from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        passenger_set = set(passengers)
        j = 0 
        for bus in buses:
            count = 0 
            while j < len(passengers) and passengers[j] <= bus and count < capacity:
                j += 1
                count += 1
        if count < capacity:
            latest_time = buses[-1]
        else: 
            latest_time = passengers[j - 1] - 1 

        while latest_time in passenger_set:
            latest_time -= 1
        return latest_time