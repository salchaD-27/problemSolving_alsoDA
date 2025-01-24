#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool searchInRow(vector<vector<int>>& matrix, int row, int target){
        for(int j=0; j<matrix[row].size(); j++){if(matrix[row][j]==target){return true;}}
        return false;
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
           for(int i=0; i<matrix.size(); i++){if(target>=matrix[i][0] && target<=matrix[i][matrix[i].size()-1]){return searchInRow(matrix, i, target);}}
           return false;
    }
};