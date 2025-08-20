#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
int moves = 0;
int dfs(struct TreeNode* node) {
    if (!node) return 0;
    int left_excess = dfs(node->left);
    int right_excess = dfs(node->right);
    moves += abs(left_excess) + abs(right_excess);
    return node->val + left_excess + right_excess - 1;
}
int distributeCoins(struct TreeNode* root) {
    moves = 0;
    dfs(root);
    return moves;
}