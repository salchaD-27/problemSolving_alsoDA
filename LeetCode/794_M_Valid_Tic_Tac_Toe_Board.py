# from typing import List
# class Solution:
#     def validTicTacToe(self, board: List[str]) -> bool:
#         xcount,ocount=0,0
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 if board[i][j]=='X': xcount+=1
#                 elif board[i][j]=='O': ocount+=1
#         if ocount>xcount: return False
#         if xcount-ocount>1: return False
#         return True

from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(player: str) -> bool:
            return any(
                all(board[i][j] == player for j in range(3)) or
                all(board[j][i] == player for j in range(3))
                for i in range(3)
            ) or (
                board[0][0] == board[1][1] == board[2][2] == player or
                board[0][2] == board[1][1] == board[2][0] == player
            )
        xcount = sum(row.count('X') for row in board)
        ocount = sum(row.count('O') for row in board)
        if ocount > xcount or xcount - ocount > 1: return False
        xwin = win('X')
        owin = win('O')
        if xwin and owin: return False
        if xwin and xcount != ocount + 1: return False
        if owin and xcount != ocount: return False
        return True