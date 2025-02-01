// #include <stdio.h>
// #include <stdlib.h>
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };
// int countNode(struct ListNode* head) {
//     int count = 0;
//     while (head) {
//         count++;
//         head = head->next;
//     }
//     return count;
// }
// int removeValInListFromIndex(struct ListNode** head, int index) {
//     struct ListNode* temp = *head;
//     if (index == 0) {
//         *head = (*head)->next;
//         int val = temp->val;
//         free(temp);
//         return val;
//     }
//     for (int i = 0; i < index - 1; i++){temp = temp->next;}
//     struct ListNode* nodeToDelete = temp->next;
//     temp->next = nodeToDelete->next;
//     int val = nodeToDelete->val;
//     free(nodeToDelete);
//     return val;
// }
// struct ListNode* insertionSortInsert(struct ListNode* head, int val) {
//     struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
//     newNode->val = val;
//     newNode->next = NULL;
//     if (head == NULL || head->val >= val) {
//         newNode->next = head;
//         return newNode;
//     }
//     struct ListNode* temp = head;
//     while (temp->next != NULL && temp->next->val < val){temp = temp->next;}
//     newNode->next = temp->next;
//     temp->next = newNode;
//     return head;
// }
// struct ListNode* sortList(struct ListNode* head){
//     if (head == NULL) return NULL;
//     struct ListNode* sorted = NULL;
//     int n = countNode(head);
//     for (int i = 0; i < n; i++) {
//         int temp = removeValInListFromIndex(&head, 0);
//         sorted = insertionSortInsert(sorted, temp);
//     }
//     return sorted;
// }

// #include <stdio.h>
// #include <stdlib.h>
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };
// struct ListNode* sortedInsert(struct ListNode* sorted, struct ListNode* newNode) {
//     if (!sorted || sorted->val >= newNode->val) {
//         newNode->next = sorted;
//         return newNode;
//     }  
//     struct ListNode* temp = sorted;
//     while (temp->next && temp->next->val < newNode->val){temp = temp->next;}
//     newNode->next = temp->next;
//     temp->next = newNode;
//     return sorted;
// }
// struct ListNode* sortList(struct ListNode* head) {
//     if (!head || !head->next) return head;
//     struct ListNode* sorted = NULL;
//     struct ListNode* current = head;
//     while (current) {
//         struct ListNode* next = current->next;
//         current->next = NULL;                  
//         sorted = sortedInsert(sorted, current);
//         current = next;                        
//     }
//     return sorted;
// }

#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* merge(struct ListNode* l1, struct ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;
    if (l1->val < l2->val) {
        l1->next = merge(l1->next, l2);
        return l1;
    } else {
        l2->next = merge(l1, l2->next);
        return l2;
    }
}
struct ListNode* findMiddle(struct ListNode* head) {
    struct ListNode* slow = head;
    struct ListNode* fast = head->next;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
struct ListNode* sortList(struct ListNode* head) {
    if (!head || !head->next) return head;
    struct ListNode* mid = findMiddle(head);
    struct ListNode* rightHalf = mid->next;
    mid->next = NULL;
    struct ListNode* leftSorted = sortList(head);
    struct ListNode* rightSorted = sortList(rightHalf);
    return merge(leftSorted, rightSorted);
}