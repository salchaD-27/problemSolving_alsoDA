from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def diff(str1, str2): return sum(1 for a, b in zip(str1, str2) if a != b)
        def findMinMutation(currentTarget, totalBank, count, visited):
            if currentTarget == startGene: return count
            
            candidates = []
            for i, gene in enumerate(totalBank):
                if gene not in visited and diff(currentTarget, gene) == 1: candidates.append(gene)
            if not candidates: return float('inf')
            min_count = float('inf')
            for candidate in candidates:
                visited.add(candidate)
                steps = findMinMutation(candidate, totalBank, count + 1, visited)
                visited.remove(candidate)
                min_count = min(min_count, steps)
            return min_count
        
        if endGene not in bank: return -1
        min_steps = findMinMutation(endGene, bank + [startGene], 0, set())
        return min_steps if min_steps != float('inf') else -1