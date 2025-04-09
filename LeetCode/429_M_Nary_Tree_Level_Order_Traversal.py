"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from typing import List
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(level_values)
        return result