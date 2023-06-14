import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next is None:
            return f'{self.val}'
        
        return f'{self.val}->{self.next.__str__()}'


class Solution:
    def reverse(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev, curr = None, head

        while curr and k:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            k -= 1
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = head
        for _ in range(k):
            if tmp is None:
                return head
            
            tmp = tmp.next

        prev = self.reverse(head, k)
        head.next = self.reverseKGroup(tmp, k)

        return prev
    

class TestListNode(unittest.TestCase):
    def testCase1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(Solution().reverseKGroup(head, 3).__str__(), '3->2->1->4->5', '3->2->1->4->5')
    def testCase2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(Solution().reverseKGroup(head, 2).__str__(), '2->1->4->3->5', '2->1->4->3->5')
    

if __name__ == '__main__':
    unittest.main()