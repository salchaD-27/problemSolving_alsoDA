#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
void dfs(struct TreeNode* tree, int maxVal, int minVal, int* diff) {
    if (tree == NULL) return;
    int currDiff = abs(maxVal - tree->val);
    if (currDiff > *diff) *diff = currDiff;
    currDiff = abs(minVal - tree->val);
    if (currDiff > *diff) *diff = currDiff;
    maxVal = (tree->val > maxVal) ? tree->val : maxVal;
    minVal = (tree->val < minVal) ? tree->val : minVal;
    dfs(tree->left, maxVal, minVal, diff);
    dfs(tree->right, maxVal, minVal, diff);
}
int maxAncestorDiff(struct TreeNode* root) {
    if (root == NULL) return 0;
    int diff = 0;  // Initialize diff as a local variable
    dfs(root, root->val, root->val, &diff);
    return diff;
}