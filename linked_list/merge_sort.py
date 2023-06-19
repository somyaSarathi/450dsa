import unittest
from typing import Optional
from ListNode import ListNode    


class Solution():
    def div(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Splits a Linked list into two
        '''
        if head.next is None:
            return head
        
        curr = head
        mid = head
        n = 0

        while curr:
            n += 1
            if n > 2 and n%2 == 0:
                mid = mid.next
            curr = curr.next

        res = mid.next
        mid.next = None

        return res
    

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Returns merge of two sorted linked lists
        '''
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        curr = l1
        prev = None

        while curr and l2:
            if curr.val < l2.val:
                prev = curr
                curr = curr.next
                continue

            insrt = l2
            l2 = l2.next

            if prev:
                prev.next = insrt
            else:
                l1 = insrt
            
            insrt.next = curr
            prev = insrt

        while l2:
            prev.next = l2
            prev = prev.next
            l2 = l2.next

        return l1
    

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        head2 = self.div(head)

        head = self.sortList(head)
        head2 = self.sortList(head2)

        return self.merge(head, head2)
        


class TestDiv(unittest.TestCase):
    def testDiv1(self):
        head  = ListNode(3, ListNode(6, ListNode(7)))
        res = Solution().div(head).__str__()

        self.assertEqual(res, '6->7', f'{res}')
        self.assertEqual(head.__str__(), '3', f'{head.__str__()}')
        

    def testDiv2(self):
        head  = ListNode(3, ListNode(6, ListNode(7, ListNode(8))))
        res = Solution().div(head).__str__()

        self.assertEqual(res, '7->8', f'{res}')
        self.assertEqual(head.__str__(), '3->6', f'{head.__str__()}')
        

    def testDiv3(self):
        head  = ListNode(3)
        res = Solution().div(head).__str__()

        self.assertEqual(res, '3', f'{res}')
        self.assertEqual(head.__str__(), '3', f'{head.__str__()}')
        

    def testDiv4(self):
        head  = ListNode(2, ListNode(1))
        res = Solution().div(head).__str__()

        self.assertEqual(res, '1', f'{res}')


    def testDiv5(self):
        head  = ListNode(3, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))
        res = Solution().div(head).__str__()

        self.assertEqual(res, '7->8->9', f'{res}')
        self.assertEqual(head.__str__(), '3->6', f'{head.__str__()}')



class TestMerge(unittest.TestCase):
    def testMerge1(self):
        l1 = ListNode(1, ListNode(2, ListNode(4, ListNode(4))))
        l2 = ListNode(2, ListNode(3))
        res = Solution().merge(l1, l2).__str__()

        self.assertEqual(res, '1->2->2->3->4->4', f'{res}')


    def testMerge2(self):
        l1 = ListNode(1, ListNode(2))
        l2 = ListNode(3, ListNode(4, ListNode(5)))
        res = Solution().merge(l1, l2).__str__()

        self.assertEqual(res, '1->2->3->4->5')


    def testMerge3(self):
        l1 = ListNode(2, ListNode(3))
        l2 = ListNode(1, ListNode(4))
        res = Solution().merge(l1, l2).__str__()

        self.assertEqual(res, '1->2->3->4')


    def testMerge4(self):
        l1 = ListNode(1, ListNode(1, ListNode(1)))
        l2 = ListNode(1, ListNode(1))
        res = Solution().merge(l2, l1).__str__()

        self.assertEqual(res, '1->1->1->1->1')



class TestSortList(unittest.TestCase):
    def testSortList1(self):
        head = ListNode(2, ListNode(4, ListNode(1, ListNode(3))))
        res = Solution().sortList(head).__str__()

        self.assertEqual(res, '1->2->3->4', f'{res}')


    def testSortList2(self):
        head = ListNode(1, ListNode(1, ListNode(1)))
        res = Solution().sortList(head).__str__()

        self.assertEqual(res, '1->1->1', f'{res}')



if __name__ == '__main__':
    unittest.main()