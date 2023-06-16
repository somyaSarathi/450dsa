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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        
        return False
    

class TestListNode(unittest.TestCase):
    def testCase1(self):
        head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
        curr, rep = head, head.next

        while curr.next:
            curr = curr.next
        curr.next = rep

        self.assertEqual(Solution().hasCycle(head), True, f'Input: head = [3,2,0,-4], pos = 1\nExpected: True\nOutput: False')

    def testCase2(self):
        head = ListNode(1, ListNode(2))
        head.next.next = head

        self.assertEqual(Solution().hasCycle(head), True, f'Input: head = [1,2], pos = 0\nExpected: True\nOutput: False')

    def testCase3(self):
        head = ListNode(1)
        self.assertEqual(Solution().hasCycle(head), False, f'Input: head = [1], pos = -1\nExpected: False\nOutput: True')


if __name__ == '__main__':
    unittest.main()
