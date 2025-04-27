from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        count = defaultdict(int)

        def postorder(node):
            if not node: return 0
            left = postorder(node.left)
            right = postorder(node.right)
            total = node.val + left + right
            count[total] += 1
            return total

        postorder(root)
        max_freq = max(count.values())
        return [s for s in count if count[s] == max_freq]