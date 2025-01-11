#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int* result;
int resultIndex;
bool visited[1000];

int* createResultArray(int size, int* index) {
    *index = 0;
    return (int*)malloc(size * sizeof(int));
}
void addToResult(int value) {
    result[resultIndex++] = value;
}
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void mapParents(struct TreeNode* node, struct TreeNode* parent, struct TreeNode** parents) {
    if (node == NULL) {
        return;
    }
    parents[node->val] = parent;
    mapParents(node->left, node, parents);
    mapParents(node->right, node, parents);
}

void visit(struct TreeNode* node, int travel, struct TreeNode** parents) {
    if (node == NULL || visited[node->val]) {
        return;
    }
    visited[node->val] = true; // Mark this node visited
    if (travel == 0) {
        addToResult(node->val);
    } else {
        visit(node->left, travel - 1, parents);
        visit(node->right, travel - 1, parents);
        struct TreeNode* parent = parents[node->val];
        visit(parent, travel - 1, parents);
    }
}

int* distanceK(struct TreeNode* root, struct TreeNode* target, int k, int* returnSize) {
    int maxSize = 1000;
    result = createResultArray(maxSize, &resultIndex);
    struct TreeNode* parents[1000] = {NULL};
    mapParents(root, NULL, parents);
    for (int i = 0; i < 1000; i++) {
        visited[i] = false;
    }
    visit(target, k, parents);
    *returnSize = resultIndex;
    return result;
}
