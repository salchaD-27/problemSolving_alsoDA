// #include <stdio.h>
// #include <stdlib.h>
// struct TreeNode {
//     int val;
//     struct TreeNode *left;
//     struct TreeNode *right;
// };
// typedef struct {
//     struct TreeNode* root;
//     struct TreeNode** queue;
//     int size;
//     int capacity;
//     int front;
//     int rear;
// } CBTInserter;
// struct TreeNode* createNode(int val) {
//     struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
//     node->val = val;
//     node->left = node->right = NULL;
//     return node;
// }
// CBTInserter* cBTInserterCreate(struct TreeNode* root) {
//     CBTInserter* tree = (CBTInserter*)malloc(sizeof(CBTInserter));
//     tree->root = root;
//     tree->capacity = 1000;
//     tree->queue = (struct TreeNode**)malloc(sizeof(struct TreeNode*) * tree->capacity);
//     tree->size = 0;
//     tree->front = 0;
//     tree->rear = 0;
//     struct TreeNode** bfs = (struct TreeNode**)malloc(sizeof(struct TreeNode*) * tree->capacity);
//     int idx = 0;
//     bfs[idx++] = root;
//     for (int i = 0; i < idx; i++) {
//         struct TreeNode* node = bfs[i];
//         if (node->left) bfs[idx++] = node->left;
//         if (node->right) bfs[idx++] = node->right;
//         if (!(node->left && node->right)) {
//             tree->queue[tree->rear++] = node;
//             tree->size++;
//         }
//     }
//     free(bfs);
//     return tree;
// }
// int cBTInserterInsert(CBTInserter* obj, int val) {
//     struct TreeNode* parent = obj->queue[obj->front];
//     struct TreeNode* newNode = createNode(val);
//     if (!parent->left) { parent->left = newNode;}
//     else {
//         parent->right = newNode;
//         obj->front++;
//     }
//     obj->queue[obj->rear++] = newNode;
//     return parent->val;
// }
// struct TreeNode* cBTInserterGet_root(CBTInserter* obj){return obj->root;}
// void cBTInserterFree(CBTInserter* obj) {
//     free(obj->queue);
//     free(obj);
// }

#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* dfs(struct TreeNode* root, int parent, int v, int* p, int cnt, int idx) {
    if (cnt == idx) {
        struct TreeNode* node = (struct TreeNode*) malloc(1 * sizeof(struct TreeNode));
        node->left = NULL;
        node->right = NULL;
        node->val = v;
        (*p) = parent;
        return node;
    }
    if (root == NULL) return NULL;
    root->left = dfs(root->left, root->val, v, p, cnt, 2*idx);
    root->right = dfs(root->right, root->val,v, p, cnt, 2*idx+1);
    return root;
}
int dfs_cnt(struct TreeNode* root) {
    if (root == NULL) return 0;
    return dfs_cnt(root->left) + dfs_cnt(root->right) + 1;
}
void dfs_free(struct TreeNode* root) {
    if (root == NULL) return;
    dfs_free(root->left);
    dfs_free(root->right);
    free(root);
}
typedef struct {
    struct TreeNode* root;
    int cnt;
} CBTInserter;
CBTInserter* cBTInserterCreate(struct TreeNode* root) {
    CBTInserter* obj = (CBTInserter*) malloc(1 * sizeof(CBTInserter));
    obj->root = root;
    obj->cnt = dfs_cnt(root);
    return obj;
}
int cBTInserterInsert(CBTInserter* obj, int val) {
    int p = -1;
    (obj->cnt)++;
    dfs(obj->root, obj->root->val, val, &p, obj->cnt, 1);
    return p;
}
struct TreeNode* cBTInserterGet_root(CBTInserter* obj){return obj->root;}
void cBTInserterFree(CBTInserter* obj){dfs_free(obj->root);}