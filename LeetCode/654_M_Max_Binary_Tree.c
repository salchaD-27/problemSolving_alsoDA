// #include <stdio.h>
// #include <stdlib.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// void createTree(struct TreeNode* lastRoot, int* remNodes, int remNodesSize, int L, int R, char toAdd){
//     if (remNodesSize == 0) return;
//     int maxIdx=0, maxElem=0;
//     for(int i=L; i<=R; i++){
//         if (remNodes[i]>maxElem){
//             maxElem=remNodes[i];
//             maxIdx=i;
//         }
//     }
//     struct TreeNode* newNode=(struct TreeNode*)malloc(sizeof(struct TreeNode));
//     newNode->left=NULL;
//     newNode->right=NULL;
//     newNode->val=maxElem;
//     if(toAdd=='L'){lastRoot->left=newNode;}
//     else{lastRoot->right=newNode;}
//     createTree(newNode, remNodes, L, maxIdx-1, remNodesSize-1, 'L');
//     createTree(newNode, remNodes, maxIdx+1, R, remNodesSize-1, 'R');
// }
// struct TreeNode* constructMaximumBinaryTree(int* nums, int numsSize) {
//     int maxIdx=0, maxElem=0;
//     for(int i=0; i<=numsSize; i++){
//         if (nums[i]>maxElem){
//             maxElem=nums[i];
//             maxIdx=i;
//         }
//     }
//     struct TreeNode* root=(struct TreeNode*)malloc(sizeof(struct TreeNode));
//     root->left=NULL;
//     root->right=NULL;
//     root->val=maxElem;
//     createTree(root, nums, 0, maxIdx-1, numsSize-1, 'L');
//     createTree(root, nums, maxIdx+1, numsSize, numsSize-1, 'R');
//     return root;
// }

#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* buildTree(int* nums, int L, int R) {
    if (L > R) return NULL;
    int maxIdx = L;
    for (int i = L + 1; i <= R; i++) {
        if (nums[i] > nums[maxIdx]) {
            maxIdx = i;
        }
    }
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = nums[maxIdx];
    node->left = buildTree(nums, L, maxIdx - 1);
    node->right = buildTree(nums, maxIdx + 1, R);
    return node;
}
struct TreeNode* constructMaximumBinaryTree(int* nums, int numsSize) {return buildTree(nums, 0, numsSize - 1);}