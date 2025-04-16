// #include <stdio.h>
// #include <stdlib.h>
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };
// int countNodes(struct ListNode* head) {
//     int count = 0;
//     while (head != NULL) {
//         count++;
//         head = head->next;
//     }
//     return count;
// }
// struct ListNode* addLists(struct ListNode* primList, struct ListNode* secList, int skips){
//     struct ListNode* head = primList;
//     while(skips){
//         head=head->next;
//         skips--;
//     }
//     while(head){
//         head->val += secList->val;
//         head = head->next;
//     }
//     return primList;
// }
// struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
//     int c1=countNodes(l1);
//     int c2=countNodes(l2);
//     if(c1>c2){
//         int skips=c1-c2;
//         return addLists(l1, l2, skips);
//     }else{
//         int skips=c2-c1;
//         return addLists(l2, l1, skips);
//     }
// }

#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* newNode(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}
int countNodes(struct ListNode* head) {
    int count = 0;
    while (head != NULL) {
        count++;
        head = head->next;
    }
    return count;
}
struct ListNode* padList(struct ListNode* head, int pad) {
    while (pad--) {
        struct ListNode* temp = newNode(0);
        temp->next = head;
        head = temp;
    }
    return head;
}
struct ListNode* addHelper(struct ListNode* l1, struct ListNode* l2, int* carry) {
    if (l1 == NULL && l2 == NULL) return NULL;
    struct ListNode* next = addHelper(l1->next, l2->next, carry);
    int sum = l1->val + l2->val + *carry;
    struct ListNode* curr = newNode(sum % 10);
    curr->next = next;
    *carry = sum / 10;
    return curr;
}
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int len1 = countNodes(l1);
    int len2 = countNodes(l2);
    if (len1 < len2) l1 = padList(l1, len2 - len1);
    else if (len2 < len1) l2 = padList(l2, len1 - len2);
    int carry = 0;
    struct ListNode* result = addHelper(l1, l2, &carry);
    if (carry > 0) {
        struct ListNode* head = newNode(carry);
        head->next = result;
        return head;
    }
    return result;
}