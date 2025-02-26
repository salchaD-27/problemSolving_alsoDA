from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y: return False
        queue = deque([(0, 0)])  
        visited = set() 
        while queue:
            a, b = queue.popleft()
            if a + b == target: return True
            if (a, b) in visited: continue
            visited.add((a, b))
            queue.append((x, b))  # Fill x
            queue.append((a, y))  # Fill y
            queue.append((0, b))  # Empty x
            queue.append((a, 0))  # Empty y
            # x -> y
            pour_x_to_y = (a - min(a, y - b), b + min(a, y - b))
            queue.append(pour_x_to_y)
            # y -> x
            pour_y_to_x = (a + min(b, x - a), b - min(b, x - a))
            queue.append(pour_y_to_x)
        return False

from math import gcd
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        return target % gcd(x, y) == 0