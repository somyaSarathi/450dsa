import unittest
from typing import Optional
from ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        prev = None
        carry = 0
        while l1 and l2:
            l1.val += l2.val + carry

            if l1.val < 10:
                carry = 0
            else:
                l1.val %= 10
                carry = 1

            prev = l1
            l1 = l1.next
            l2 = l2.next

        while l1:
            l1.val += carry

            if l1.val < 10:
                carry = 0
            else:
                l1.val %= 10
                carry = 1

            prev = l1
            l1 = l1.next

        while l2:
            prev.next = ListNode(l2.val + carry)
            prev = prev.next

            if prev.val < 10:
                carry = 0
            else:
                prev.val %= 10
                carry = 1

            l2 = l2.next

        if carry:
            prev.next = ListNode(1)

        return head
    

class TestListNode(unittest.TestCase):
    def testCase1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        res = Solution().addTwoNumbers(l1, l2).__str__()

        self.assertEqual(res, '7->0->8', f'\nInput: l1=[2,4,3], l2=[5,6,5]\nExpected: [7,0,8]\nOutput: {res}')


    def testCase2(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        res = Solution().addTwoNumbers(l1, l2).__str__()

        self.assertEqual(res, '0', f'\nInput: l1=[0], l2=[0]\nExpected: [0]\nOutput: {res}')


    def testCase3(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        res = Solution().addTwoNumbers(l1, l2).__str__()

        self.assertEqual(res, '8->9->9->9->0->0->0->1', f'\nInput: l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]\nExpected: [8,9,9,9,0,0,0,1]\nOutput: {res}')
    

if __name__ == '__main__':
    unittest.main()