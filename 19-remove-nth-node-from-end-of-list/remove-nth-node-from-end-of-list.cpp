class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* slow = head;
        ListNode* fast = head;
        for(int i = 0; i < n; i++){
            fast = fast->next;
        }
        if(fast == nullptr){
            ListNode* delNode = head;
            head = head->next;
            delete delNode;
            return head;
        }
        while(fast->next != nullptr){
            slow = slow->next;
            fast = fast->next;
        }
        ListNode* delNode = slow->next;
        slow->next = slow->next->next;
        delete delNode;
        return head;
    }
};