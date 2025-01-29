#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int max(int a, int b){return (a > b) ? a : b;}
int dfs(struct TreeNode* node, int* max_sum) {
    if (!node) return 0;
    int left_max = max(0, dfs(node->left, max_sum));
    int right_max = max(0, dfs(node->right, max_sum));
    int current_path_sum = node->val + left_max + right_max;
    *max_sum = max(*max_sum, current_path_sum);
    return node->val + max(left_max, right_max);
}
int maxPathSum(struct TreeNode* root) {
    int max_sum = INT_MIN;
    dfs(root, &max_sum);
    return max_sum;
}