#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_NODES 1000
#define HASH_SIZE 10007
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
typedef struct HashNode {
    char *key;
    int count;
    struct TreeNode *node;
    struct HashNode *next;
} HashNode;
HashNode* hashMap[HASH_SIZE];
struct TreeNode* result[MAX_NODES];
int resultSize = 0;
unsigned int hash(char *str) {
    unsigned int h = 0;
    while (*str) {h = (h * 31 + *str++) % HASH_SIZE;}
    return h;
}
void addToHashMap(char *key, struct TreeNode *node) {
    unsigned int idx = hash(key);
    HashNode *entry = hashMap[idx];
   
    while (entry) {
        if (strcmp(entry->key, key) == 0) {
            entry->count++;
            if (entry->count == 2) {result[resultSize++] = node;}
            return;
        }
        entry = entry->next;
    }
    entry = (HashNode *)malloc(sizeof(HashNode));
    entry->key = strdup(key);
    entry->count = 1;
    entry->node = node;
    entry->next = hashMap[idx];
    hashMap[idx] = entry;
}
char* serialize(struct TreeNode* root) {
    if (!root) {return strdup("#");}
    char *left = serialize(root->left);
    char *right = serialize(root->right);
    int size = strlen(left) + strlen(right) + 50;
    char *buffer = (char *)malloc(size);
    snprintf(buffer, size, "%d,%s,%s", root->val, left, right);
    addToHashMap(buffer, root);
    free(left);
    free(right);
    return buffer;
}
struct TreeNode** findDuplicateSubtrees(struct TreeNode* root, int* returnSize) {
    resultSize = 0;
    memset(hashMap, 0, sizeof(hashMap));
    serialize(root);
    *returnSize = resultSize;
    return result;
}