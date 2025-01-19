// if arr[0]==0, skip
// for arr[i] find next element equal or greater (calculate water hold capacity for this range)(ans+=result)
// skip to end of this range and repeat step 2 and 3

// #include <iostream>
// #include <vector>
// class Solution {
// public:
//     int nextEOG(int index, std::vector<int>& height) {
//         int val = height[index];
//         for (int j = index + 1; j < height.size(); j++){if (height[j] >= val){return j;}}
//         return -1;
//     }
//     int holdCapacity(int i, int j, std::vector<int>& height) {
//         int hold = 0;
//         for (int k = i + 1; k < j; k++){hold += std::max(0, height[i] - height[k]);}
//         return hold;
//     }
//     int trap(std::vector<int>& height) {
//         int capacity = 0, n = height.size();
//         if (n < 3) return 0;
//         for (int i = 0; i < n - 1;) {
//             if (height[i] == 0) {
//                 i++;
//                 continue;
//             }
//             int j = nextEOG(i, height);
//             if (j == -1){break;}
//             capacity += holdCapacity(i, j, height);
//             i = j;
//         }
//         return capacity;
//     }
// };

#include <iostream>
#include <vector>
#include <algorithm>
class Solution {
public:
    int trap(std::vector<int>& height) {
        int n = height.size();
        if (n < 3) return 0;
        int left = 0, right = n - 1, leftMax = 0, rightMax = 0, water = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax){leftMax = height[left];} 
                else{water += leftMax - height[left];}
                ++left;
            }
            else{
                if (height[right] >= rightMax){rightMax = height[right];}
                else{water += rightMax - height[right];}
                --right;
            }
        }
        return water;
    }
};