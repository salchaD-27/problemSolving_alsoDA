#include <stdio.h>
#include <stdlib.h>
struct Node {
    int val;
    int numNeighbors;
    struct Node** neighbors;
};
struct Node* cloneDFS(struct Node* node, struct Node** clonedArray) {
    if (!node) return NULL;
    if (clonedArray[node->val]) return clonedArray[node->val];
    struct Node* clone = (struct Node*)malloc(sizeof(struct Node));
    clone->val = node->val;
    clone->numNeighbors = node->numNeighbors;
    clone->neighbors = (struct Node**)malloc(node->numNeighbors * sizeof(struct Node*));
    clonedArray[node->val] = clone;
    for (int i = 0; i < node->numNeighbors; i++){clone->neighbors[i] = cloneDFS(node->neighbors[i], clonedArray);}
    return clone;
}
struct Node* cloneGraph(struct Node* s) {
    if (!s) return NULL;
    struct Node* clonedArray[101] = {NULL};
    return cloneDFS(s, clonedArray);
}