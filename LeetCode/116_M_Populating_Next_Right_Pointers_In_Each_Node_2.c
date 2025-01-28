#include <stdio.h>
#include <stdlib.h>
struct Node {
    int val;
    struct Node *left;
    struct Node *right;
    struct Node *next;
};
struct Node* connect(struct Node* root) {
    if (!root) return root;
    struct Node* current = root; 
    while (current) {
        struct Node dummy; 
        dummy.next = NULL;
        struct Node* temp = &dummy; 
        while (current) {
            if (current->left) {
                temp->next = current->left;
                temp = temp->next;
            }
            if (current->right) {
                temp->next = current->right;
                temp = temp->next;
            }
            current = current->next;
        }
        current = dummy.next;
    }
    return root;
}