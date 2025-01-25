// #include <stdio.h>
// #include <stdbool.h>
// int binarySearch(int* arr, int low, int high, int x) {
//     while (low <= high) {
//         int mid = low + (high - low) / 2;
//         if (arr[mid] == x) return mid;
//         if (arr[mid] < x) low = mid + 1;
//         else high = mid - 1;
//     }
//     return -1;
// }
// bool search(int* nums, int numsSize, int target) {
//     int low = 0, high = numsSize - 1;
//     while (low < high) {
//         int mid = low + (high - low) / 2;
//         if (nums[mid] > nums[high]) low = mid + 1;
//         else high = mid;
//     }
//     int pivot = low;
//     if (target >= nums[pivot] && target <= nums[numsSize - 1]) {
//         if(binarySearch(nums, pivot, numsSize - 1, target)!=-1){return true;}
//     } else {
//         if(binarySearch(nums, 0, pivot - 1, target)!=-1){return true;}
//     }
//     return false;
// }

#include <stdio.h>
#include <stdbool.h>
int binarySearch(int* arr, int low, int high, int x) {
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == x) return mid;
        if (arr[mid] < x) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}
bool search(int* nums, int numsSize, int target) {
    int low = 0, high = numsSize - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) return true;
        if (nums[low] == nums[mid] && nums[mid] == nums[high]) {
            low++;
            high--;
        }
        else if (nums[low] <= nums[mid]) {
            if (nums[low] <= target && target < nums[mid]){high = mid - 1;}
            else{low = mid + 1;}
        } else {
            if (nums[mid] < target && target <= nums[high]){low = mid + 1;}
            else{high = mid - 1;}
        }
    }
    return false;
}