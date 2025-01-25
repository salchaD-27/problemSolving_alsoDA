// from typing import List
// class Solution:
//     def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
//         def smaller(index, nums):
//             val = nums[index]
//             for i in range(index):
//                 if nums[i] > val: return True
//             return False
//         def nextBigger(j, nums):
//             for i in range(j):
//                 if nums[i] > nums[j] and abs(nums[i] - nums[j]) <= limit: return i
//             return -1
        
//         for _ in range(len(nums)):
//             for j in range(len(nums)):
//                 if smaller(j, nums):
//                     swap_index = nextBigger(j, nums)
//                     if swap_index != -1: nums[j], nums[swap_index] = nums[swap_index], nums[j]
//         return nums

#include <iostream>
using namespace std;
class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        vector<int> numsSorted(nums);
        sort(numsSorted.begin(), numsSorted.end());
        int currGroup = 0;
        unordered_map<int, int> numToGroup;
        numToGroup.insert(pair<int, int>(numsSorted[0], currGroup));
        unordered_map<int, list<int>> groupToList;
        groupToList.insert(pair<int, list<int>>(currGroup, list<int>(1, numsSorted[0])));
        for (int i = 1; i < nums.size(); i++) {
            if (abs(numsSorted[i] - numsSorted[i - 1]) > limit){currGroup++;}
            numToGroup.insert(pair<int, int>(numsSorted[i], currGroup));
            if (groupToList.find(currGroup) == groupToList.end()){groupToList[currGroup] = list<int>();}
            groupToList[currGroup].push_back(numsSorted[i]);
        }
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int group = numToGroup[num];
            nums[i] = *groupToList[group].begin();
            groupToList[group].pop_front();
        }
        return nums;
    }
};