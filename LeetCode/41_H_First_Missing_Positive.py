# #include <iostream>
# using namespace std;

# class Solution {
# public:
#     void bubbleSort(vector<int>& v) {
#         int n = v.size();
#         for (int i = 0; i < n - 1; i++){for (int j = 0; j < n - i - 1; j++){if (v[j] > v[j + 1]){swap(v[j], v[j + 1]);}}}
#     }
#     int firstMissingPositive(vector<int>& nums) {
#         bubbleSort(nums);
#         int ans=1, firstPos;
#         for(int i=0; i<nums.size(); i++){
#             if(nums[i]>0){
#                 firstPos=i; 
#                 break;
#             }
#         }
#         for(int i=firstPos; i<nums.size(); i++){
#             if(nums[i]!=ans){return ans;}
#             else{ans++;}
#         }
#         return ans;
#     }
# };

# from typing import List
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         ref=[i for i in range(1, len(nums)+2)]
#         for num in ref:
#             if num not in nums: return num

# from typing import List
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         ref=[i for i in range(1, max(nums)+2)]
#         for num in nums:
#             try: ref.remove(num)
#             except ValueError: continue
#         return ref[0]
    
# from typing import List
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         ref=[i for i in range(1, len(nums)+2)]
#         for num in nums:
#             try: ref.remove(num)
#             except ValueError: continue
#         return ref[0]

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1: return i + 1
        return n + 1