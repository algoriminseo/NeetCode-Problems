/**
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
       if(head == null) {
            return null;
        }

        ListNode node = head;
        if(head.next != null) {
            node = ReverseList(head.next);
            head.next.next = head;
        }
        head.next = null;

        return node;
    }
}