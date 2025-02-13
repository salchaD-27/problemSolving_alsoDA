function neighboursSum(board: number[][], i: number, j: number): number {
    let sum = 0;
    let directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];
    for (let [dx, dy] of directions) {
        let ni = i + dx, nj = j + dy;
        if (ni >= 0 && ni < board.length && nj >= 0 && nj < board[0].length){sum += board[ni][nj];}
    }
    return sum;
}
function gameOfLife(board: number[][]): void {
    let rows = board.length, cols = board[0].length;
    let newBoard = Array.from({ length: rows }, () => Array(cols).fill(0));
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            let neighbors = neighboursSum(board, i, j);
            if (board[i][j] === 0 && neighbors === 3){newBoard[i][j] = 1;}
            else if (board[i][j] === 1 && (neighbors === 2 || neighbors === 3)){newBoard[i][j] = 1;}
            else{newBoard[i][j] = 0;}
        }
    }
    for (let i = 0; i < rows; i++){for (let j = 0; j < cols; j++){board[i][j] = newBoard[i][j];}}
}