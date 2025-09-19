#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int sum(struct TreeNode* root){
    if(root==NULL){return 0;}
    return (root->val+sum(root->left)+sum(root->right));
}
void inorder(struct TreeNode * root,int *sumn){
    if(root==NULL)
    return ;
    inorder((root->left),sumn);
    int c=root->val;
    root->val=*sumn;
    *sumn=*sumn-c;
    inorder(root->right,sumn);
}
struct TreeNode* bstToGst(struct TreeNode* root) {
    int s=sum(root);
    inorder(root,&s);
    return root;
}