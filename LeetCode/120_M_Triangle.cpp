// #include <iostream>
// using namespace std;
// class Solution {
// public:
//     int minimumTotal(vector<vector<int>>& triangle) {
//         int j=0, sum=triangle[0][j];
//         for(int i=1; i<triangle.size(); i++){
//             if(triangle[i][j]>triangle[i][j+1]){j++;}
//             sum+=triangle[i][j];
//         }
//         return sum;
//     }
// };

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        for (int i = triangle.size() - 2; i >= 0; i--) {for (int j = 0; j < triangle[i].size(); j++){triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);}}
        return triangle[0][0];
    }
};