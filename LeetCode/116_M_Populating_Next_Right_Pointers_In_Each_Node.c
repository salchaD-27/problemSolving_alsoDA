#include <stdio.h>
#include <stdlib.h>
struct Node {
    int val;
    struct Node *left;
    struct Node *right;
    struct Node *next;
};
struct Node* connect(struct Node* root) {
    if (!root || !root->left || !root->right){return root;}
    // Left to Right of same parent
    root->left->next = root->right;
    // Right to Left of other parent
    if (root->next){root->right->next = root->next->left;}
    // Left and Right subtrees
    connect(root->left);
    connect(root->right);
    return root;
}