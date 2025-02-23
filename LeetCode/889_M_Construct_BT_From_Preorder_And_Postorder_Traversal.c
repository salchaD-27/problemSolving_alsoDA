#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left, *right;
};
struct TreeNode* createNode(int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}
struct TreeNode* constructFromPrePostUtil(int* preorder, int* postorder, int* preIndex, int l, int h, int size) {
    if (*preIndex >= size || l > h) return NULL;
    struct TreeNode* root = createNode(preorder[*preIndex]);
    (*preIndex)++;
    if (l == h) return root;
    int i;
    for (i = l; i <= h; i++) {if (preorder[*preIndex] == postorder[i]){break;}}
    if (i <= h) {
        root->left = constructFromPrePostUtil(preorder, postorder, preIndex, l, i, size);
        root->right = constructFromPrePostUtil(preorder, postorder, preIndex, i + 1, h - 1, size);
    }
    return root;
}
struct TreeNode* constructFromPrePost(int* preorder, int preorderSize, int* postorder, int postorderSize) {
    int preIndex = 0;
    return constructFromPrePostUtil(preorder, postorder, &preIndex, 0, preorderSize - 1, preorderSize);
}