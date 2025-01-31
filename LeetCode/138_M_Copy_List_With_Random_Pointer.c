// #include <stdio.h>
// #include <stdlib.h>
// struct Node {
//     int val;
//     struct Node *next;
//     struct Node *random;
// };
// struct Node* cloneDFS(struct Node* node, struct Node** clonedArray) {
//     if (!node) return NULL;
//     if (clonedArray[node->val]) return clonedArray[node->val];
//     struct Node* clone = (struct Node*)malloc(sizeof(struct Node));
//     clone->val = node->val;
//     clone->next = NULL;
//     clone->random = NULL;
//     clonedArray[node->val] = clone;
//     clone->next = cloneDFS(node->next, clonedArray);
//     clone->random = cloneDFS(node->random, clonedArray);
//     return clone;
// }
// struct Node* copyRandomList(struct Node* head) {
//     if (!head) return NULL;   
//     struct Node* clonedArray[101] = {NULL};
//     return cloneDFS(head, clonedArray);
// }

#include <stdio.h>
#include <stdlib.h>
struct Node {
    int val;
    struct Node *next;
    struct Node *random;
};
struct Node* copyRandomList(struct Node* head) {
    if (!head) return NULL;
    struct Node* curr = head;
    while (curr) {
        struct Node* clone = (struct Node*)malloc(sizeof(struct Node));
        clone->val = curr->val;
        clone->next = curr->next;
        clone->random = NULL;
        curr->next = clone;
        curr = clone->next;
    }
    curr = head;
    while (curr) {
        if (curr->random){curr->next->random = curr->random->next;}
        curr = curr->next->next;
    }
    curr = head;
    struct Node* newHead = head->next;
    struct Node* cloneCurr = newHead;
    while (curr) {
        curr->next = cloneCurr->next;
        curr = curr->next;
        if (curr) {
            cloneCurr->next = curr->next;
            cloneCurr = cloneCurr->next;
        }
    }
    return newHead;
}