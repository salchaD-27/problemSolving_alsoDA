class Solution:
    def movesToChessboard(self, board):
        n = len(board)
        # validity
        for row in board:
            for col in range(n):
                if board[0][0] ^ board[0][col] ^ row[0] ^ row[col]: return -1
        rowSum = sum(board[0])
        colSum = sum(board[i][0] for i in range(n))
        rowSwap = sum(board[0][i] == i % 2 for i in range(n))
        colSwap = sum(board[i][0] == i % 2 for i in range(n))
        if not (n // 2 <= rowSum <= (n + 1) // 2): return -1
        if not (n // 2 <= colSum <= (n + 1) // 2): return -1
        if n % 2 == 0:
            rowSwap = min(rowSwap, n - rowSwap)
            colSwap = min(colSwap, n - colSwap)
        else:
            if rowSwap % 2: rowSwap = n - rowSwap
            if colSwap % 2: colSwap = n - colSwap
        return (rowSwap + colSwap) // 2