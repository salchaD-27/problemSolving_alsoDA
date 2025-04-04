#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* createNode(int val) {
    struct TreeNode* newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->val = val;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}
struct Result {
    int depth;
    struct TreeNode* lca;
};
struct Result dfs(struct TreeNode* node) {
    struct Result res;
    if (node == NULL) {
        res.depth = 0;
        res.lca = NULL;
        return res;
    }  
    struct Result leftRes = dfs(node->left);
    struct Result rightRes = dfs(node->right);
    if (leftRes.depth == rightRes.depth) {
        res.depth = leftRes.depth + 1;
        res.lca = node;
    } 
    else if (leftRes.depth > rightRes.depth) {
        res.depth = leftRes.depth + 1;
        res.lca = leftRes.lca;
    }
    else {
        res.depth = rightRes.depth + 1;
        res.lca = rightRes.lca;
    }
    
    return res;
}
struct TreeNode* lcaDeepestLeaves(struct TreeNode* root) {
    struct Result result = dfs(root);
    return result.lca;
}