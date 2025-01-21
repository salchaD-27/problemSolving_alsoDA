// from typing import List
// class Solution:
//     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
//         //            right   down    left      up
//         direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
//         direcIndex = 0
//         topBound = 0
//         rightBound = len(matrix[0])
//         bottomBound = len(matrix)
//         leftBound = 0
//         x, y = 0, 0
//         result = []
//         while len(result) < len(matrix) * len(matrix[0]):  
//             result.append(matrix[x][y])  
//             nx, ny = x + direction[direcIndex][0], y + direction[direcIndex][1]
//             if nx < topBound or nx >= bottomBound or ny < leftBound or ny >= rightBound:
//                 if direcIndex == 0: topBound += 1
//                 elif direcIndex == 1: rightBound -= 1
//                 elif direcIndex == 2: bottomBound -= 1
//                 elif direcIndex == 3: leftBound += 1
//                 direcIndex = (direcIndex + 1) % 4  
//             x += direction[direcIndex][0]
//             y += direction[direcIndex][1]
//         return result


#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()){return {};}
        //                     right    down   left      up
        int direction[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int direcIndex = 0;
        int topBound = 0, bottomBound = matrix.size(), leftBound = 0, rightBound = matrix[0].size();
        int x = 0, y = 0;
        vector<int> result;
        while (result.size() < matrix.size() * matrix[0].size()) {
            result.push_back(matrix[x][y]);
            int nx = x + direction[direcIndex][0];
            int ny = y + direction[direcIndex][1];
            if (nx < topBound || nx >= bottomBound || ny < leftBound || ny >= rightBound) {
                if (direcIndex == 0){topBound++;}
                else if (direcIndex == 1){rightBound--;}
                else if (direcIndex == 2){bottomBound--;}
                else if (direcIndex == 3){leftBound++;}
                direcIndex = (direcIndex + 1) % 4;
            }
            x += direction[direcIndex][0];
            y += direction[direcIndex][1];
        }
        return result;
    }
};