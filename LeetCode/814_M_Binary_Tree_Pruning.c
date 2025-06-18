// #include <stdio.h>
// #include <stdlib.h>
// #include <stdbool.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// bool has1(struct TreeNode* root){
//     if(root->val!=1 && root->left==NULL && root->right==NULL){return false;}
//     if(root->val==1 && root->left==NULL && root->right==NULL){return true;}
//     return has1(root->left) || has1(root->right);
// }
// void prune(struct TreeNode* root){
//     if(root==NULL){return;}
//     bool leftHas=has1(root->left), rightHas=has1(root->right);
//     if(!leftHas){root->left=NULL;}
//     if(!rightHas){root->right=NULL;}
//     if(root->val!=1){root=NULL;}
//     prune(root->left);
//     prune(root->right);
//     return;
// }
// struct TreeNode* pruneTree(struct TreeNode* root) {
//     if(root==NULL){return NULL;}
//     prune(root);
//     return root;
// }

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* pruneTree(struct TreeNode* root) {
    if (root == NULL) return NULL;
    root->left = pruneTree(root->left);
    root->right = pruneTree(root->right);
    if (root->val == 0 && root->left == NULL && root->right == NULL) {
        free(root);
        return NULL;
    }
    return root;
}
