from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []  # to store all intersecting intervals
        i = j = 0  # Initialize pointers for both lists
        # While both lists have unprocessed intervals
        while i < len(firstList) and j < len(secondList):
            # Calculate the start and end of the potential intersection
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            # If there's a valid intersection, add it to the result list
            if start <= end: intersections.append([start, end])
            # Move forward in the list with the earlier ending interval
            if firstList[i][1] < secondList[j][1]: i += 1
            else: j += 1
        return intersections