// #include <stdio.h>
// #include <stdlib.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// struct TreeNode** generateTreesInRange(int start, int end, int* returnSize) {
//     if (start > end) {
//         *returnSize = 1;
//         struct TreeNode** result = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
//         result[0] = NULL;
//         return result;
//     }
//     struct TreeNode** all_trees = NULL;
//     int count = 0;
//     for (int i = start; i <= end; i++) {
//         int leftSize = 0;
//         int rightSize = 0;
//         struct TreeNode** leftTrees = generateTreesInRange(start, i - 1, &leftSize);
//         struct TreeNode** rightTrees = generateTreesInRange(i + 1, end, &rightSize);
//         for (int leftIdx = 0; leftIdx < leftSize; leftIdx++) {
//             for (int rightIdx = 0; rightIdx < rightSize; rightIdx++) {
//                 struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
//                 root->val = i;
//                 root->left = leftTrees[leftIdx];
//                 root->right = rightTrees[rightIdx];
//                 all_trees = (struct TreeNode**)realloc(all_trees, sizeof(struct TreeNode*) * (count + 1));
//                 all_trees[count] = root;
//                 count++;
//             }
//         }
//         free(leftTrees);
//         free(rightTrees);
//     }
//     *returnSize = count;
//     return all_trees;
// }
// struct TreeNode** generateTrees(int n, int* returnSize) {
//     if (n == 0) {
//         *returnSize = 0;
//         return NULL;
//     }
//     return generateTreesInRange(1, n, returnSize);
// }
// int numTrees(int n) {
//     int returnSize = 0;
//     struct TreeNode** trees = generateTrees(n, &returnSize);
//     return returnSize;
// }

#include <stdio.h>
int numTrees(int n) {
    if (n == 0) return 0;
    int dp[n+1];
    dp[0] = 1;
    dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = 0;
        for (int j = 1; j <= i; j++){dp[i] += dp[j-1] * dp[i-j];}
    }
    return dp[n];
}