// #include <stdio.h>
// #include <stdlib.h>
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };
// struct ListNode* insertEnd(struct ListNode* head, int val) {
//     struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode));
//     temp->val = val;
//     temp->next = NULL;
//     if(!head){return temp;}
//     struct ListNode* ptr = head;
//     while(ptr->next){ptr = ptr->next;}
//     ptr->next = temp;
//     return head;
// }
// int toNum(struct ListNode* head) {
//     int num=0, power=1;
//     while(head != NULL){
//         num+=(head->val)*power;
//         power*=10;
//         head=head->next;
//     }
//     return num;
// }
// struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
//     int num1=toNum(l1), num2=toNum(l2), ans=num1+num2;
//     struct ListNode* l3 = NULL;
//     if(ans == 0){
//         struct ListNode* l3 = (struct ListNode*)malloc(sizeof(struct ListNode));
//         l3->val = 0;
//         l3->next = NULL;
//         return l3;
//     }
//     while(ans!=0){
//         int temp=ans%10;
//         l3=insertEnd(l3, temp);
//         ans/=10;
//     }
//     return l3;
// }



#include <stdio.h>
#include <stdlib.h>
struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* insertEnd(struct ListNode* head, int val) {
    struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode));
    temp->val = val;
    temp->next = NULL;
    if(!head){return temp;}
    struct ListNode* ptr = head;
    while(ptr->next){ptr = ptr->next;}
    ptr->next = temp;
    return head;
}
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* l3 = NULL;
    int carry=0;
    while (l1 != NULL || l2 != NULL || carry != 0) {
        int val1 = l1 ? l1->val : 0, val2 = l2 ? l2->val : 0, sum = val1 + val2 + carry;
        carry = sum / 10;
        l3 = insertEnd(l3, sum % 10);
        if (l1) l1 = l1->next; 
        if (l2) l2 = l2->next; 
    }
    return l3;
}