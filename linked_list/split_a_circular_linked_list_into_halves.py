import unittest
from typing import Optional
from ListNode import ListNode

class Solution:
    def div(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        
        curr = head
        mid = head
        n = 0

        while curr:
            n += 1
            if n > 2 and n%2 != 0:
                mid = mid.next
            curr = curr.next

        res = mid.next
        mid.next = None

        return head, res
    

    def splitList(self, head: Optional[ListNode]) -> Optional[tuple[ListNode]]:
        if head is None:
            return None, None
        
        if head.next is None:
            head.next = None
            return head, None
        
        curr = head.next
        while curr:
            if curr.next == head:
                curr.next = None
            curr = curr.next

        return self.div(head)


class TestListNode(unittest.TestCase):
    def testCase1(self):
        head = ListNode(1)
        head.next = ListNode(2, ListNode(4, head))
        a, b = Solution().splitList(head)

        self.assertEqual(str(a), '1->2', f'{a.__str__()}')
        self.assertEqual(str(b), '4', f'{b.__str__()}')


    def testCase2(self):
        head = ListNode(1)
        head.next = ListNode(2, ListNode(4, ListNode(6, head)))
        a, b = Solution().splitList(head)

        self.assertEqual(str(a), '1->2', f'{a.__str__()}')
        self.assertEqual(str(b), '4->6', f'{b.__str__()}')


if __name__ == '__main__':
    unittest.main()