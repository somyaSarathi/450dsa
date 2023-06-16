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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        visited = dict()
        i = 0
        while curr:
            if curr in visited:
                return curr
            
            visited[curr] = i
            curr = curr.next
            i += 1

        return None
    

class TestListNode(unittest.TestCase):
    def testCase1(self):
        head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
        curr, rep = head, head.next

        while curr.next:
            curr = curr.next
        curr.next = rep

        res = Solution().detectCycle(head)

        self.assertEqual(res, rep, f'Input: head = [3,2,0,-4], pos = 1\nExpected: 2')

    def testCase2(self):
        head = ListNode(1, ListNode(2))
        head.next.next = head

        res = Solution().detectCycle(head)

        self.assertEqual(res, head, f'Input: head = [1,2], pos = 0\nExpected: 1')

    def testCase3(self):
        head = ListNode(1)

        res = Solution().detectCycle(head)
        self.assertEqual(res, None, f'Input: head = [1], pos = -1\nExpected: None')


if __name__ == '__main__':
    unittest.main()