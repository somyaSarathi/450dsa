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
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        
        return prev
    

class TestListNode(unittest.TestCase):
    def testCase1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(Solution().reverse(head).__str__(), '5->4->3->2->1', '5->4->3->2->1')

    def testCase2(self):
        head = ListNode(1, ListNode(2))
        self.assertEqual(Solution().reverse(head).__str__(), '2->1', '2->1')

    def testCase3(self):
        self.assertEqual(Solution().reverse(None), None, '[]')
    

if __name__ == '__main__':
    unittest.main()