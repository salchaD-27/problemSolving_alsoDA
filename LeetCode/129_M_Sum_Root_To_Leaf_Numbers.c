#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int sumOfPath(struct TreeNode* root, int sumSoFar) {
    if (root == NULL) return 0;
    sumSoFar = sumSoFar * 10 + root->val;
    if (root->left == NULL && root->right == NULL){return sumSoFar;}
    return sumOfPath(root->left, sumSoFar) + sumOfPath(root->right, sumSoFar);
}
int sumNumbers(struct TreeNode* root){return sumOfPath(root, 0);}