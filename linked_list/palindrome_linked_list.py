import unittest
from typing import Optional
from ListNode import ListNode



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ''
        while head:
            s += str(head.val)
            head = head.next

        return s == s[::-1]
    


class TestListNode(unittest.TestCase):
    def testCase1(self):
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        res = Solution().isPalindrome(head)

        self.assertEqual(res, True, f'{res}')
    

    def testCase2(self):
        head = ListNode(1, ListNode(2, ListNode(2)))
        res = Solution().isPalindrome(head)

        self.assertEqual(res, False, f'{res}')



if __name__ == '__main__':
    unittest.main()