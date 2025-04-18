#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* findMin(struct TreeNode* node) {
    while (node->left != NULL){node = node->left;}
    return node;
}
struct TreeNode* deleteNode(struct TreeNode* root, int key) {
    if (root == NULL) return NULL;
    if (key < root->val) {root->left = deleteNode(root->left, key);}
    else if (key > root->val) {root->right = deleteNode(root->right, key);}
    // Node found
    else {
        if (root->left == NULL) {
            struct TreeNode* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct TreeNode* temp = root->left;
            free(root);
            return temp;
        } else {
            // Node with two children
            struct TreeNode* minNode = findMin(root->right);
            root->val = minNode->val;
            root->right = deleteNode(root->right, minNode->val);
        }
    }
    return root;
}