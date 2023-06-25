from TreeNode import TreeNode
from typing import Optional


class Solution:
    def dfs(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        return  max( self.dfs(root.left, depth+1), self.dfs(root.right, depth+1) )
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)