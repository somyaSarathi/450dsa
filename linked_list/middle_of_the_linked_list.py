from typing import Optional
from ListNode import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        
        curr = head
        mid = head
        n = 0

        while curr:
            n += 1
            if n > 2 and n%2 == 0:
                mid = mid.next
            curr = curr.next

        res = mid.next

        return res