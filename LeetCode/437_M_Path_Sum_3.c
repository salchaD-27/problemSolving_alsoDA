// #include <stdio.h>
// #include <stdlib.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// int subPathSum(struct TreeNode* root, int remainingSum, int count){
//     if((remainingSum==0)||(root==NULL)){return count;}
//     // root = remaining sum
//     if(root->val==remainingSum){
//         count++;
//         return count;
//     }
//     // root < remaining sum
//     if(root->val<remainingSum){return subPathSum(root->left,remainingSum-root->val,count)+subPathSum(root->right,remainingSum-root->val,count);}
//     // root > remaining sum
//     return;

// }
// int pathSum(struct TreeNode* root, int targetSum) {return subPathSum(root,targetSum,0);}

#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int countPaths(struct TreeNode* root, long targetSum) {
    if (root == NULL) return 0;
    int count = 0;
    if (root->val == targetSum) count++;
    count += countPaths(root->left, targetSum - root->val);
    count += countPaths(root->right, targetSum - root->val);
    return count;
}
int pathSum(struct TreeNode* root, int targetSum) {
    if (root == NULL) return 0;
    return countPaths(root, targetSum) + pathSum(root->left, targetSum) + pathSum(root->right, targetSum);
}