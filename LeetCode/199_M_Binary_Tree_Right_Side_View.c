// #include <stdio.h>
// #include <stdlib.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };

// int countNodes(struct TreeNode* root){
//     if(root->left==NULL && root->right==NULL){return 1;}
//     int count=1;
//     count+=countNode(root->left)+countNode(root->right);
//     return count;
// }
// int* traverse(struct TreeNode* root, int* ans, int levelsVisited){
//     if(root->left==NULL && root->right==NULL){return ans;}
//     if(root->left!=NULL && root->right==NULL){
//         ans[levelsVisited++]=root->left->val;
//         ans=traverse(root, ans, levelsVisited);
//     }
//     if(root->left==NULL && root->right!=NULL){
//         ans[levelsVisited++]=root->right->val;
//         ans=traverse(root->right, ans, levelsVisited);
//     }
//     return ans;
// }
// int* rightSideView(struct TreeNode* root, int* returnSize) {
//     int* ans = (int*)malloc(countNodes(root)*sizeof(int));
//     int levelsVisited=0;
//     ans[levelsVisited++]=root->val;
//     if(root->right!=NULL){
//         ans=traverse(root->right, ans, levelsVisited);
//     }
// }

#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
void dfs(struct TreeNode* root, int level, int* ans, int* maxLevel, int* index) {
    if (root == NULL) return;
    if (level > *maxLevel) {
        ans[*index] = root->val;
        (*index)++;
        *maxLevel = level;
    }
    dfs(root->right, level + 1, ans, maxLevel, index);
    dfs(root->left, level + 1, ans, maxLevel, index);
}
int* rightSideView(struct TreeNode* root, int* returnSize) {
    if (root == NULL) {
        *returnSize = 0;
        return NULL;
    }
    int* ans = (int*)malloc(100 * sizeof(int));
    int maxLevel = -1, index = 0;
    dfs(root, 0, ans, &maxLevel, &index);
    *returnSize = index;
    return ans;
}