# #include <stdio.h>
# #include <stdlib.h>
# typedef struct TreeNode {
#     int val;
#     struct TreeNode *left, *right;
# };
# struct TreeNode* newNode(int val) {
#     struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
#     node->val = val;
#     node->left = node->right = NULL;
#     return node;
# }
# struct TreeNode* buildAVL(int start, int end) {
#     if (start > end) return NULL;
#     int mid = (start + end + 1) / 2;
#     struct TreeNode* root = newNode(mid);
#     root->left = buildAVL(start, mid - 1);
#     root->right = buildAVL(mid + 1, end); 
#     return root;
# }
# int sumRightmostPath(struct TreeNode* root) {
#     if (root == NULL || root->right == NULL) return 0;
#     int sum = 0;
#     while (root->right != NULL) {
#         sum += root->val;
#         root = root->right;
#     }
#     return sum;
# }
# int getMoneyAmount(int n) {
#     struct TreeNode* root = buildAVL(1, n);
#     return sumRightmostPath(root);
# }

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for length in range(2, n + 1):  
            for i in range(1, n - length + 2):  
                j = i + length - 1 
                dp[i][j] = float('inf')
                for k in range(i, j + 1):
                    cost = k + max(dp[i][k - 1] if k > i else 0, dp[k + 1][j] if k < j else 0)
                    dp[i][j] = min(dp[i][j], cost) 
        return dp[1][n]