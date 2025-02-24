#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
void dfs(struct TreeNode* root, int* result) {
    if (root == NULL) {
        result[0] = 0; // withRoot
        result[1] = 0; // withoutRoot
        return;
    }
    int left[2] = {0, 0};
    int right[2] = {0, 0};
    dfs(root->left, left);
    dfs(root->right, right);
    result[0] = root->val + left[1] + right[1];
    result[1] = (left[0] > left[1] ? left[0] : left[1]) + (right[0] > right[1] ? right[0] : right[1]);
}
int rob(struct TreeNode* root) {
    int result[2] = {0, 0};
    dfs(root, result);
    return result[0] > result[1] ? result[0] : result[1];
}