#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
// int countNodes(struct ListNode* head) {
//     int count = 0;
//     while (head) {
//         count++;
//         head = head->next;
//     }
//     return count;
// }
// struct ListNode* appendNode(struct ListNode* head, int val) {
//     struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
//     newNode->val = val;
//     newNode->next = NULL;
//     if (!head) return newNode;
//     struct ListNode* temp = head;
//     while (temp->next) temp = temp->next;
//     temp->next = newNode;
//     return head;
// }
// struct ListNode* deleteNextNode(struct ListNode* head, struct ListNode* temp) {
//     if (!temp || !temp->next) return head;   
//     struct ListNode* ptr = temp->next;
//     temp->next = ptr->next;
//     free(ptr);
//     return head;
// }
// struct ListNode* oddEvenList(struct ListNode* head) {
//     struct ListNode* temp=head;
//     int nodes=countNodes(head);
//     for(int i=0; i<nodes; i++){
//         if(i%2!=0){head=appendNode(head, temp->val);}
//         temp=temp->next;
//     }
//     for(int i=0; i<nodes; i++){
//         if(i%2==0){head=deleteNextNode(head, temp);}
//         temp=temp->next;
//     }
//     return head;
// }
struct ListNode* oddEvenList(struct ListNode* head) {
    if (!head || !head->next) return head;
    struct ListNode* odd = head;
    struct ListNode* even = head->next;
    struct ListNode* evenHead = even;
    while (even && even->next) {
        odd->next = even->next;
        odd = odd->next;
        even->next = odd->next;
        even = even->next;
    }
    odd->next = evenHead;
    return head;
}