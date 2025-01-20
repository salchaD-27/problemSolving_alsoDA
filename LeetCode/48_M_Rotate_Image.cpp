// 00 01 02
// 10 11 12
// 20 21 22

// 00 01 02
//    11

// 00 01 02 03
// 10 11 12 13
// 20 21 22 23
// 30 31 32 33

// 00 01 02 03
//    11 12

#include <iostream>
#include <vector>
class Solution {
public:
    void rotateCells(vector<vector<int>>& matrix, int i, int j){
            int n=matrix.size(), temp = matrix[i][j];
            matrix[i][j] = matrix[n - j - 1][i];
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
            matrix[j][n - i - 1] = temp;
    }
    void rotate(vector<vector<int>>& matrix) {
        int n=matrix.size();
        for(int i=0; i<n/2; i++){for(int j=i; j<n-i-1; j++){rotateCells(matrix, i, j);}}
    }
};