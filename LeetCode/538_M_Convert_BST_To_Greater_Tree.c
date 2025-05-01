#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
void convertHelper(struct TreeNode* root, int* sum) {
    if (root == NULL) return;
    convertHelper(root->right, sum);
    root->val += *sum;
    *sum = root->val;
    convertHelper(root->left, sum);
}
struct TreeNode* convertBST(struct TreeNode* root) {
    // traversal: right -> root -> left
    // new value of node = new value of parent + sum total of right subtree
    int sum = 0;
    convertHelper(root, &sum);
    return root;
}