from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0:
            return list(range(len(security)))
        
        n = len(security)
        nonIncDays = [0] * n
        for i in range(1, n):
            if security[i] <= security[i - 1]: nonIncDays[i] = nonIncDays[i - 1] + 1
        nonDecDays = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]: nonDecDays[i] = nonDecDays[i + 1] + 1

        goodDays = []
        for i in range(time, n - time):
            if nonIncDays[i] >= time and nonDecDays[i] >= time:
                goodDays.append(i)

        return goodDays