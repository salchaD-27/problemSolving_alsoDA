#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int getDeepest(struct TreeNode* root) {
    if (!root) return 0;
    int left = getDeepest(root->left);
    int right = getDeepest(root->right);
    return 1 + (left > right ? left : right);
}
struct TreeNode* dfs(struct TreeNode* root, int depth, int targetDepth) {
    if (!root) return NULL;
    if (depth == targetDepth) return root;
    struct TreeNode* left = dfs(root->left, depth + 1, targetDepth);
    struct TreeNode* right = dfs(root->right, depth + 1, targetDepth);
    if (left && right) return root;
    return left ? left : right;
}
struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root) {
    int deepest = getDeepest(root);
    return dfs(root, 1, deepest);
}