from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        st = [root,None]
        ans = [[]]
        ind = 0
        while st:
            temp = st.pop(0)
            if not temp:
                ind +=1
                if st:
                    st.append(None)
                    ans.append([])
            else:
                ans[ind].append(temp.val)
                if temp.right: st.append(temp.right)
                if temp.left: st.append(temp.left)
        return sum(ans[-1])