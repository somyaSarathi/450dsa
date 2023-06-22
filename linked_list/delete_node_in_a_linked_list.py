from typing import Optional
from ListNode import ListNode


class Solution:
    def deleteNode(self, node: ListNode[Optional]) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node:
            if node.next.next is None:
                node.val = node.next.val
                node.next = None
                break
            node.val = node.next.val
            node = node.next

        return
