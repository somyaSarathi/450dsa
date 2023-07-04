from TreeNode import TreeNode
from typing import Optional


class Solution:
    def nodes(self, root: Optional[TreeNode], h=0, res=None) -> dict[int, list[int]]:
        if res is None:
            res = dict()
            
        if root is None:
            return res
        
        res[h] = root.val

        if root.left:
            res = self.nodes(root.left, h+1, res)
        if root.right:
            res = self.nodes(root.right, h+1, res)

        return res
    

    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = self.nodes(root)
        return list(res.values())



if __name__ == '__main__':
    root = TreeNode( 1, TreeNode( 2, TreeNode( 4, right=TreeNode( 7, right=TreeNode(9) ) ), TreeNode(5) ), TreeNode( 3, TreeNode( 6, right=TreeNode(8) ) ) )

    print(Solution().rightSideView(root))