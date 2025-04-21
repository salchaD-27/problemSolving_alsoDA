# [1, -3, 4]
# [x, x+1, x+1-3, x+1-3+4]
# [x, x+1, x-2, x+2]
# low=x-2 (>=1) ,so, x-2>=1 => x>=3
# high=x+2 (<=6) ,so, x+2<=6 => x<=4
# => x=3,4

from typing import List
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        tempHidden=[0]
        for i in range(len(differences)):
            tempHidden.append(tempHidden[-1]+differences[i])
        low=min(tempHidden)
        high=max(tempHidden)
        start=lower-low
        end=upper-high
        return max(0,end-start+1)

from typing import List
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        tempHidden=[0]
        for i in range(len(differences)):
            tempHidden.append(tempHidden[-1]+differences[i])
        return max(0,((upper-max(tempHidden))-(lower-min(tempHidden))+1))