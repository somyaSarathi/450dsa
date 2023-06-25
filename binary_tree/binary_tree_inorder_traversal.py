from TreeNode import TreeNode
from typing import Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        return [] if not root else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)