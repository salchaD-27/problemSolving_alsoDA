from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        def validRow(row):
            nums = set()
            for num in row:
                if num != '.' and num in nums: return False
                nums.add(num)
            return True
        for row in board:
            if not validRow(row): return False

        # columns
        def validColumn(board, col):
            nums = set()
            for i in range(len(board)):
                if board[i][col] != '.' and board[i][col] in nums: return False
                nums.add(board[i][col])
            return True
        for i in range(9):
            if not validColumn(board, i): return False

        # subBlocks
        def validSubBlock(board, x1, y1, x2, y2):
            nums = set()
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if board[i][j] != '.' and board[i][j] in nums: return False
                    nums.add(board[i][j])
            return True
        subBlocks=[[0,0,2,2],[0,3,2,5],[0,6,2,8],[3,0,5,2],[3,3,5,5],[3,6,5,8],[6,0,8,2],[6,3,8,5],[6,6,8,8]]
        for block in subBlocks:
            x1, y1, x2, y2 = block
            if not validSubBlock(board, x1, y1, x2, y2): return False

        # finalTrue
        return True