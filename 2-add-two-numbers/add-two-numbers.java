/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2){
        ListNode L = new ListNode(0);
        ListNode Current = L;

        int carry = 0;
        while(l1!=null||l2!=null||carry!=0){
            int sum = carry;
            if(l1!=null){
                sum+=l1.val;
                l1 = l1.next; // move forward
            }
            if(l2!=null){
                sum+=l2.val;
                l2 = l2.next; // move forward
            }

            carry = sum/10; // forward carry
            int digit = sum%10; // actual digit

            // next creation
            Current.next = new ListNode(digit);
            Current = Current.next; // point to next
        }       
        return L.next; // skiping the 0
    }
}