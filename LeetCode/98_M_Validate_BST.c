// #include <stdio.h>
// #include <stdlib.h>
// #include <stdbool.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// bool isValidRoot(struct TreeNode* root){
//     // Base, Leaf
//     if(root->left==NULL && root->right==NULL){return true;}
//     // Recursive, Right
//     if(root->left==NULL && root->right!=NULL && root->right->val>=root->val){return (true && isValidRoot(root->right));}
//     else{return false;}
//     // Recursive, Left
//     if(root->right==NULL && root->left!=NULL && root->left->val<=root->val){return (true && isValidRoot(root->left));;}
//     else{return false;}
//     // Recursive, Others
//     if(root->left!=NULL && root->right!=NULL){return (isValidRoot(root->left) && isValidRoot(root->right));}
// }
// bool isValidBST(struct TreeNode* root){return isValidRoot(root);}

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
bool isValidRoot(struct TreeNode* root, long long minVal, long long maxVal) {
    if (root == NULL){return true;}
    if (root->val <= minVal || root->val >= maxVal){return false;}
    return isValidRoot(root->left, minVal, root->val) && isValidRoot(root->right, root->val, maxVal);
}
bool isValidBST(struct TreeNode* root){return isValidRoot(root, LLONG_MIN, LLONG_MAX);}