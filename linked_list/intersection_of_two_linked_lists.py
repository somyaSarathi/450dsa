import unittest
from typing import Optional
from ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = set()
        while headA:
            a.add(headA)
            headA = headA.next

        while headB:
            if headB in a:
                return headB
            headB = headB.next

        return None
    

class TestListNode(unittest.TestCase):
    def testCase1(self):
        common = ListNode(8, ListNode(4, ListNode(5)))
        headA = ListNode(4, ListNode(1, common))
        headB = ListNode(5, ListNode(6, ListNode(1, common)))
        res = Solution().getIntersectionNode(headA, headB)

        self.assertEqual(res, common, f'\nInput: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3\nExpected: Intersected at "8"\nOutput: {res.val}')

    def testCase2(self):
        common = ListNode(2, ListNode(4))
        headA = ListNode(1, ListNode(9, ListNode(1, common)))
        headB = ListNode(3, common)
        res = Solution().getIntersectionNode(headA, headB)

        self.assertEqual(res, common, f'\nintersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1\nExpected: Intersected at "2"\nOutput: {res.val}')

    def testCase3(self):
        headA = ListNode(2, ListNode(6, ListNode(4)))
        headB = ListNode(1, ListNode(5))
        res = Solution().getIntersectionNode(headA, headB)

        self.assertEqual(res, None, f"\nInput: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2\nExpected: No intersection\nOutput: {res}")


if __name__ == '__main__':
    unittest.main()