#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
void helper(struct TreeNode* root, int val, int currDepth, int targetDepth) {
    if (!root) return;
    if (currDepth == targetDepth - 1) {
        struct TreeNode* newLeft = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newLeft->val = val;
        newLeft->left = root->left;
        newLeft->right = NULL;
        root->left = newLeft;
        struct TreeNode* newRight = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newRight->val = val;
        newRight->right = root->right;
        newRight->left = NULL;
        root->right = newRight;
    } else {
        helper(root->left, val, currDepth + 1, targetDepth);
        helper(root->right, val, currDepth + 1, targetDepth);
    }
}
struct TreeNode* addOneRow(struct TreeNode* root, int val, int depth) {
    if (depth == 1) {
        struct TreeNode* newRoot = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        newRoot->val = val;
        newRoot->left = root;
        newRoot->right = NULL;
        return newRoot;
    }
    helper(root, val, 1, depth);
    return root;
}