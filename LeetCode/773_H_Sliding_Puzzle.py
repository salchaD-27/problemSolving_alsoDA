from typing import List
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(num) for row in board for num in row)
        target = '123450'
        neighbors = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        visited = set()
        queue = deque([(start, 0)])  # (state, steps)
        while queue:
            state, steps = queue.popleft()
            if state == target: return steps
            zero_idx = state.index('0')
            for neighbor in neighbors[zero_idx]:
                lst = list(state)
                lst[zero_idx], lst[neighbor] = lst[neighbor], lst[zero_idx]
                new_state = ''.join(lst)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
        return -1