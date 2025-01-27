#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
void inorder(struct TreeNode* root, struct TreeNode** prev, struct TreeNode** first, struct TreeNode** second) {
    if (root == NULL){return;}
    inorder(root->left, prev, first, second);
    if (*prev && (*prev)->val > root->val) {
        if (*first == NULL){*first = *prev; }
        *second = root;
    }
    *prev = root;
    inorder(root->right, prev, first, second);
}
void recoverTree(struct TreeNode* root) {
    struct TreeNode *first = NULL, *second = NULL, *prev = NULL;
    inorder(root, &prev, &first, &second);
    if (first && second){swap(&(first->val), &(second->val));}
}