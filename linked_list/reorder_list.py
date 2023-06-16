import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f'{self.val}'
        return f'{self.val}->{self.next.__str__()}'


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return head
        
        n = 0               # length of the linked list
        curr = head
        order = dict()      # store the node index

        while curr:
            order[n] = curr
            curr = curr.next
            n += 1

        if n < 3:
            return head

        for i in range(n//2):
            if n//2-1 == i and n%2 == 0:
                continue

            curr = order[i]
            forward = curr.next
            newNext = order[n-i-1]

            curr.next = newNext
            newNext.next = forward

            order[n-i-2].next = None

        return head
    

class TestListNode(unittest.TestCase):
    def testCase1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        res = Solution().reorderList(head).__str__()

        self.assertEqual( res, '1->4->2->3', f'Input: 1->2->3->4\nExpected: 1->4->2->3\nOutput: {res}')
    
    def testCase2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        res = Solution().reorderList(head).__str__()

        self.assertEqual( res, '1->5->2->4->3', f'Input: 1->2->3->4->5\nExpected: 1->5->2->4->3\nOutput: {res}')
    

if __name__ == '__main__':
    unittest.main()