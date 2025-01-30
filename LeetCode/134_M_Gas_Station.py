from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        totalCost = 0
        currentGas = 0
        startIndex = 0
        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            currentGas += gas[i] - cost[i]
            if currentGas < 0:
                startIndex = i + 1
                currentGas = 0

        if totalGas < totalCost: return -1
        return startIndex