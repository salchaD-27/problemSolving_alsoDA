from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit: left += 1  # lightest boards with heaviest
            right -= 1  # heaviest always boards
            boats += 1
        return boats