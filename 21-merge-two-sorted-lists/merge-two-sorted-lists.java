class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode thead = list1;
        if(list1 == null && list2 == null)
            return list1;
        if(list1 == null)
            return list2;
        if(list2 == null)
            return list1;
        if(list1.val > list2.val){
            thead = list2;
            ListNode temp2 = list1;
            list1 = list2;
            list2 = temp2;
        }
        while(list1 != null && list2 != null){
            if(list1.val <= list2.val){
                list1 = list1.next;
            }else{
                ListNode temp = list1.next;
                list1.next = list2;
                list2 = list2.next;
                list1.next.next = temp;
                //swaping values
                int tempval = list1.val;
                list1.val = list1.next.val;
                list1.next.val = tempval;
                list1 = list1.next;
            }
        }
        if(list2 != null){
            ListNode thead1 = thead; 
            while(thead1.next != null){
                thead1 = thead1.next;
            }
            thead1.next = list2;
        }
        return thead;
    }
}