from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root: return []
            return dfs(root.left)+[root.val]+dfs(root.right)
        return sorted(dfs(root1)+dfs(root2))