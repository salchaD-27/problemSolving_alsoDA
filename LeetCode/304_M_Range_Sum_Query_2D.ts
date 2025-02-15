// class NumMatrix {
//     private numMat: number[][];
//     constructor(matrix: number[][]) {this.numMat = matrix.map(row => [...row]); }
//     sumRegion(row1: number, col1: number, row2: number, col2: number): number {
//         let sum: number = 0;
//         for (let i = row1; i <= row2; i++) {for (let j = col1; j <= col2; j++) {sum += this.numMat[i][j];}}
//         return sum;
//     }
// }

class NumMatrix {
    private prefixSum: number[][];
    constructor(matrix: number[][]) {
        let rows = matrix.length, cols = matrix[0].length;
        this.prefixSum = Array.from({ length: rows + 1 }, () => Array(cols + 1).fill(0));
        for (let i = 1; i <= rows; i++) {
            for (let j = 1; j <= cols; j++) {
                this.prefixSum[i][j] =
                    matrix[i - 1][j - 1] +
                    this.prefixSum[i - 1][j] + 
                    this.prefixSum[i][j - 1] - 
                    this.prefixSum[i - 1][j - 1];
            }
        }
    }
    sumRegion(row1: number, col1: number, row2: number, col2: number): number {
        return (
            this.prefixSum[row2 + 1][col2 + 1] -
            this.prefixSum[row1][col2 + 1] -
            this.prefixSum[row2 + 1][col1] +
            this.prefixSum[row1][col1]
        );
    }
}