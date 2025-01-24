#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void setRowZero(vector<vector<int>>& matrix, int row){for (int j = 0; j < matrix[row].size(); j++){matrix[row][j] = 0;}}
    void setColZero(vector<vector<int>>& matrix, int col){for (int i = 0; i < matrix.size(); i++){matrix[i][col] = 0;}}
    void setZeroes(vector<vector<int>>& matrix) {
        vector<pair<int, int>> matrixZeroes;
        for (int i = 0; i < matrix.size(); i++){for (int j = 0; j < matrix[i].size(); j++){if (matrix[i][j] == 0){matrixZeroes.push_back({i, j});}}}
        for (const auto& zero : matrixZeroes) {
            setRowZero(matrix, zero.first);
            setColZero(matrix, zero.second);
        }
    }
};