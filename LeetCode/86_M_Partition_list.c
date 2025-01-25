// #include <stdio.h>
// #include <stdlib.h>
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };
// struct ListNode* removeAndReinsert(struct ListNode* head, int index){
//     if (head == NULL || head->next == NULL) return head;
//     struct ListNode* ptr = head;
//     struct ListNode* rem = head;
//     for(int i = 0; i < index; i++){ptr = ptr->next;}
//     rem = ptr->next;
//     ptr->next = rem->next;
//     struct ListNode* temp = head;
//     while (temp->next != NULL && temp->next->val <= rem->val){temp = temp->next;}
//     rem->next = temp->next;
//     temp->next = rem;
//     return head;
// }
// struct ListNode* partition(struct ListNode* head, int x) {
//     struct ListNode* temp = head;
//     int index = 0;
//     while (temp != NULL && temp->next != NULL) {
//         if (temp->val < x){head = removeAndReinsert(head, index);}
//         temp = temp->next;
//         index++;
//     }
//     return head;
// }

#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* createNode(int value) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = value;
    newNode->next = NULL;
    return newNode;
}
struct ListNode* partition(struct ListNode* head, int x) {
    struct ListNode *lessHead = NULL, *greaterHead = NULL;
    struct ListNode *lessTail = NULL, *greaterTail = NULL;
    struct ListNode* temp = head;
    while (temp != NULL) {
        struct ListNode* newNode = createNode(temp->val);
        if (temp->val < x) {
            if (lessHead == NULL) {
                lessHead = newNode;
                lessTail = newNode;
            } else {
                lessTail->next = newNode;
                lessTail = newNode;
            }
        } else {
            if (greaterHead == NULL) {
                greaterHead = newNode;
                greaterTail = newNode;
            } else {
                greaterTail->next = newNode;
                greaterTail = newNode;
            }
        }
        temp = temp->next;
    }
    if (lessHead != NULL) {
        lessTail->next = greaterHead;
        return lessHead;
    }
    return greaterHead;
}