#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* createNode(int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}
struct TreeNode* recoverFromPreorder(char* traversal) {
    if (!traversal || traversal[0] == '\0') return NULL;
    struct TreeNode* stack[1000]; 
    int top=-1;                
    int i=0;
    while (traversal[i] != '\0') {
        int depth = 0;
        while (traversal[i] == '-') {
            depth++;
            i++;
        }
        int num = 0;
        while (traversal[i] >= '0' && traversal[i] <= '9') {
            num = num * 10 + (traversal[i] - '0');
            i++;
        }
        struct TreeNode* node = createNode(num);
        top = depth - 1;
        if (top >= 0) {
            if(stack[top]->left == NULL){stack[top]->left = node;}
            else{stack[top]->right = node;}
        }
        stack[++top] = node;
    }
    return stack[0]; 
}