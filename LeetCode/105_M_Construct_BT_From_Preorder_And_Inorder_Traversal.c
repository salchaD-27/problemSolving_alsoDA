#include <stdlib.h>
#include <stdio.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* buildTreeRecursive(int* preorder, int* inorder, int preorderStart, int preorderEnd, int inorderStart, int inorderEnd) {
    // Base case
    if (preorderStart > preorderEnd || inorderStart > inorderEnd){return NULL;}
    // First in preorder is root
    int rootVal = preorder[preorderStart];
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = rootVal;
    root->left = root->right = NULL;
    // Root's index in inorder
    int rootIndexInorder = inorderStart;
    while (inorder[rootIndexInorder] != rootVal){rootIndexInorder++;}
    // Nodes in left subtree
    int leftSize = rootIndexInorder - inorderStart;
    // Recursively build left subtree
    root->left = buildTreeRecursive(preorder, inorder, preorderStart + 1, preorderStart + leftSize, inorderStart, rootIndexInorder - 1);
    // Recursively build right subtree
    root->right = buildTreeRecursive(preorder, inorder, preorderStart + leftSize + 1, preorderEnd, rootIndexInorder + 1, inorderEnd);
    return root;
}
struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize){return buildTreeRecursive(preorder, inorder, 0, preorderSize - 1, 0, inorderSize - 1);}