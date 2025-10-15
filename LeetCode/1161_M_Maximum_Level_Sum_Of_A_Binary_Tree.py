from collections import deque
class Solution:
    def maxLevelSum(self, root):
        if not root: return 0
        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        current_level = 1

        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            current_level += 1
        return max_level