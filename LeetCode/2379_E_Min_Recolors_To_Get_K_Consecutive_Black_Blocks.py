# W B B W W B B W B W
# _ B B _ _ B B _ B _
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolors = float('inf')
        current_whites = sum(1 for i in range(k) if blocks[i] == 'W')
        min_recolors = min(min_recolors, current_whites)
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W': current_whites -= 1
            if blocks[i] == 'W': current_whites += 1
            min_recolors = min(min_recolors, current_whites)
        return min_recolors