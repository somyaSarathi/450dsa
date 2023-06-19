from typing import Optional
from ListNode import ListNode


class Solution:
    def isCircular(head: Optional[ListNode]) -> bool:
        # Code here
        if head is None:
            return True
            
        curr = head.next
        
        while curr:
            if curr == head:
                return True
            curr = curr.next
            
        return False