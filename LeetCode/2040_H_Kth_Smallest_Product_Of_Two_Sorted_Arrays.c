// #include <stdio.h>
// #include <stdlib.h>
// #include <limits.h>

// void add(long long* arr, int k, long long val) {
//     int indexToInsert = 0;
//     for (int i = 0; i < k; i++) {if (arr[i] < val){indexToInsert++;}}
//     for (int i = k - 1; i > indexToInsert; i--){arr[i] = arr[i - 1];}
//     arr[indexToInsert] = val;
// }

// long long kthSmallestProduct(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
//     long long res[k];
//     for (int i = 0; i < k; i++){res[i] = LLONG_MAX;}
//     for (int i = 0; i < nums1Size; i++) {
//         for (int j = 0; j < nums2Size; j++) {
//             long long product = (long long)nums1[i] * (long long)nums2[j];
//             if (product < res[k - 1]){add(res, k, product);}
//         }
//     }
//     return res[k - 1];
// }


#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

long long countLessOrEqual(int* nums1, int nums1Size, int* nums2, int nums2Size, long long target) {
    long long count = 0;
    for (int i = 0; i < nums1Size; i++) {
        if (nums1[i] < 0) { // For negative numbers
            int left = 0, right = nums2Size;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if ((long long)nums1[i] * nums2[mid] <= target) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            count += nums2Size - right;
        } else if (nums1[i] > 0) { // For positive numbers
            int left = 0, right = nums2Size;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if ((long long)nums1[i] * nums2[mid] <= target) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            count += left;
        } else { // For zero
            if (target >= 0) {
                count += nums2Size;
            }
        }
    }
    return count;
}

long long kthSmallestProduct(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    // Determine the search space for products
    long long left = (long long)nums1[0] * nums2[0];
    long long right = (long long)nums1[nums1Size - 1] * nums2[nums2Size - 1];

    for (int i = 0; i < nums1Size; i++) {
        if ((long long)nums1[i] * nums2[0] < left) left = (long long)nums1[i] * nums2[0];
        if ((long long)nums1[i] * nums2[nums2Size - 1] > right) right = (long long)nums1[i] * nums2[nums2Size - 1];
    }

    long long result = 0;

    // Perform binary search to find the k-th smallest product
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if (countLessOrEqual(nums1, nums1Size, nums2, nums2Size, mid) >= k) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return result;
}