#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* helper(int* preorder, int* i, int n, int bound) {
    if (*i >= n || preorder[*i] > bound) return NULL;
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = preorder[(*i)++];
    root->left = helper(preorder, i, n, root->val);
    root->right = helper(preorder, i, n, bound);
    return root;
}
struct TreeNode* bstFromPreorder(int* preorder, int n) {
    int i = 0;
    return helper(preorder, &i, n, INT_MAX);
}