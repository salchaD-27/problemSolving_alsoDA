// #include <stdio.h>
// #include <stdlib.h>
// #include <stdbool.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// bool descendant(struct TreeNode* anc, struct TreeNode* des) {
//     if (anc == NULL){return false;}
//     if (anc->val == des->val){return true;}
//     return descendant(anc->left, des) || descendant(anc->right, des);
// }
// struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
//     if(descendant(p, q)){return p;}
//     else if(descendant(q, p)){return q;}
//     else{return root;}
// }

#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    if (root == NULL) return NULL;
    if (root == p || root == q) return root;
    struct TreeNode* left = lowestCommonAncestor(root->left, p, q);
    struct TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if (left != NULL && right != NULL) return root;
    return left != NULL ? left : right;
}