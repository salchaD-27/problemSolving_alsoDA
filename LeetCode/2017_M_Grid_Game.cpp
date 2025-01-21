#include <vector>
#include <algorithm>
#include <climits>
using namespace std;
class Solution {
public:
    long long gridGame(vector<vector<int>>& grid) {
        int n = grid[0].size();
        vector<long long> top_prefix(n, 0), bottom_prefix(n, 0);
        top_prefix[0] = grid[0][0];
        bottom_prefix[0] = grid[1][0];
        for (int i = 1; i < n; i++) {
            top_prefix[i] = top_prefix[i - 1] + grid[0][i];
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i];
        }
        
        long long result = LLONG_MAX;
        for (int i = 0; i < n; i++) {
            long long top_remaining = (i < n - 1) ? (top_prefix[n - 1] - top_prefix[i]) : 0;
            long long bottom_collected = (i > 0) ? bottom_prefix[i - 1] : 0;
            long long second_robot_score = max(top_remaining, bottom_collected);
            result = min(result, second_robot_score);
        }
        return result;
    }
};