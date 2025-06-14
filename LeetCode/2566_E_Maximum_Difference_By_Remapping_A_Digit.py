class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        maxNum,minNum=float('-inf'),float('inf')
        for i in range(10):
            temp = num_str.replace(str(i), '9')
            maxNum = max(maxNum, int(temp))
        for i in range(1, 10):
            temp = num_str.replace(str(i), '0')
            minNum = min(minNum, int(temp))
        return maxNum - minNum