#include <stdlib.h>
#include <stdio.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* buildTreeRecursive(int* inorder, int* postorder, int inorderStart, int inorderEnd, int postorderStart, int postorderEnd) {
    // Base case
    if (inorderStart > inorderEnd || postorderStart > postorderEnd){return NULL;}
    // Last in postorder is root
    int rootVal = postorder[postorderEnd];
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = rootVal;
    root->left = root->right = NULL;
    // Root's index in inorder
    int rootIndexInorder = inorderStart;
    while (inorder[rootIndexInorder] != rootVal){rootIndexInorder++;}
    // Nodes in left subtree
    int leftSize = rootIndexInorder - inorderStart;
    // Recursively build right subtree (postorder reduced by 1 element for right subtree)
    root->right = buildTreeRecursive(inorder, postorder, rootIndexInorder + 1, inorderEnd, postorderStart + leftSize, postorderEnd - 1);
    // Recursively build left subtree
    root->left = buildTreeRecursive(inorder, postorder, inorderStart, rootIndexInorder - 1, postorderStart, postorderStart + leftSize - 1);
    return root;
}
struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize){return buildTreeRecursive(inorder, postorder, 0, inorderSize - 1, 0, postorderSize - 1);}