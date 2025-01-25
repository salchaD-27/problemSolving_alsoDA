from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(board, word, nextWordIndex, currentX, currentY, visited):
            if nextWordIndex == len(word): return True
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited.add((currentX, currentY))
            for dx, dy in directions:
                newX, newY = currentX + dx, currentY + dy
                if (0 <= newX < len(board) and 0 <= newY < len(board[0]) and (newX, newY) not in visited and board[newX][newY] == word[nextWordIndex]):
                    if search(board, word, nextWordIndex + 1, newX, newY, visited): return True
            visited.remove((currentX, currentY))
            return False

        start = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]: start.append((i, j))
        if not start: return False
        for x, y in start:
            if search(board, word, 1, x, y, set()): return True
        return False