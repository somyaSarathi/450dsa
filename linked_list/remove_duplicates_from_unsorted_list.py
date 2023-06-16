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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev = head
        curr = head.next

        visited = {head.val}

        while curr:
            if curr.val in visited:
                prev.next = curr.next
                curr = curr.next
                continue
            
            visited.add(curr.val)

            prev = curr
            curr = curr.next

        return head
    

class TestListNode(unittest.TestCase):
    def testCase1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(1, ListNode(4, ListNode(2))))))
        self.assertEqual(Solution().deleteDuplicates(head).__str__(), '1->2->3->4', '1->2->3->1->4->2\n1->2->3->4')

    def testCase2(self):
        head = ListNode(3, ListNode(3, ListNode(3)))
        self.assertEqual(Solution().deleteDuplicates(head).__str__(), '3', '3->3->3\n3')

    def testCase3(self):
        self.assertEqual(None, None, 'None')
    

if __name__ == '__main__':
    unittest.main()