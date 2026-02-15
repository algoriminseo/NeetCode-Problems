# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0 
        length = 0 
        tmp = head
        while tmp:
            tmp = tmp.next
            length += 1
        target_ind = length - n

        res = head
        while res:
            if target_ind == 0:
                return head.next

            if (index + 1) == target_ind:
                res.next = res.next.next
                break
            res = res.next
            index += 1

        return head
        