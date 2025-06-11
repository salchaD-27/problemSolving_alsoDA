from typing import List
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def getDist(srcX, srcY, tarX, tarY): return abs(tarX - srcX) + abs(tarY - srcY)
        myDist=getDist(0,0,target[0], target[1])
        for i in range(len(ghosts)):
            if getDist(ghosts[i][0], ghosts[i][1], target[0], target[1])<=myDist: return False
        return True