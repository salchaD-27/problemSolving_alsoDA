#include <iostream>
#include <climits>
using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum=0, ans=INT_MIN;
        for(int i=0; i<nums.size(); i++){
            sum+=nums[i];
            ans=max(ans, sum);
            sum=max(sum, 0);
        }
        return ans;
    }
};