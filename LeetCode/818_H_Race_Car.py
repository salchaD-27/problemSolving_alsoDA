from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])  # pos,speed
        visited = set((0, 1))
        steps = 0
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                if pos == target: return steps
                # A
                new_pos = pos + speed
                new_speed = speed * 2
                if (new_pos, new_speed) not in visited and 0 <= new_pos <= 2 * target:
                    queue.append((new_pos, new_speed))
                    visited.add((new_pos, new_speed))
                # R
                rev_speed = -1 if speed > 0 else 1
                if (pos, rev_speed) not in visited:
                    queue.append((pos, rev_speed))
                    visited.add((pos, rev_speed))
            steps += 1

        return -1