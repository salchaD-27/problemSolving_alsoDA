function searchMatrix(matrix: number[][], target: number): boolean {
    for(let i=0; i<matrix.length; i++){
        for(let j=0; j<matrix[i].length; j++){
            if(matrix[i][j]>target){break}
            if(matrix[i][j]===target){return true}
        }
    }
    return false
};