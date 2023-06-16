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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = head
        curr = head.next

        while curr:
            if curr.val == prev.val:
				# tmp = curr
                prev.next = curr.next
                curr = curr.next
				# del tmp
                continue
            prev = curr
            curr = curr.next

        return head
    

class TestListNode(unittest.TestCase):
    def testCase1(self):
        head = ListNode(1, ListNode(1, ListNode(2)))
        res = Solution().deleteDuplicates(head)

        self.assertEqual(res.__str__(), '1->2', f'Input: 1->1->2\nExpected: 1->2\nOutput: {res}')
    
    def testCase2(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        res = Solution().deleteDuplicates(head)

        self.assertEqual(res.__str__(), '1->2->3', f'Input: 1->1->2->3->3\nExpected: 1->2->3\nOutput: {res}')


if __name__ == '__main__':
    unittest.main()