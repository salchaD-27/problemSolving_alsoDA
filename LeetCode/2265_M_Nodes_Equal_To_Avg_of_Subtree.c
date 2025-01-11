#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int ansNodes = 0;
void avgSubtree(struct TreeNode* root, int *sum, int *nodes) {
    if (root == NULL) {
        *sum = 0;
        *nodes = 0;
        return;
    }
    int leftSum = 0, leftNodes = 0;
    int rightSum = 0, rightNodes = 0;
    avgSubtree(root->left, &leftSum, &leftNodes);
    avgSubtree(root->right, &rightSum, &rightNodes);

    *sum = leftSum + rightSum + root->val;
    *nodes = leftNodes + rightNodes + 1;
    if (*sum / *nodes == root->val) {
        ansNodes++;
    }
}
struct TreeNode* createNode(int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}
int averageOfSubtree(struct TreeNode* root) {
    ansNodes = 0;
    int sum = 0, nodes = 0;
    avgSubtree(root, &sum, &nodes);
    return ansNodes;
}