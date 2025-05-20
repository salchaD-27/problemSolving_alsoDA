#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int max(int a, int b) {return a > b ? a : b;}
int dfs(struct TreeNode* root, int* maxLen) {
    if (!root) return 0;
    int left = dfs(root->left, maxLen);
    int right = dfs(root->right, maxLen);
    int leftPath = 0, rightPath = 0;
    if (root->left && root->left->val == root->val) {leftPath = left + 1;}
    if (root->right && root->right->val == root->val) {rightPath = right + 1;}
    *maxLen = max(*maxLen, leftPath + rightPath);
    return max(leftPath, rightPath);
}
int longestUnivaluePath(struct TreeNode* root) {
    int maxLen = 0;
    dfs(root, &maxLen);
    return maxLen;
}