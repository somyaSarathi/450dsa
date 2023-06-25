import unittest
from TreeNode import TreeNode
from typing import Optional



class Solution:
    def levelOrder(self, root: Optional[TreeNode], lvl=0, nodes=None) -> list[list[int]]:
        if nodes is None:
            nodes = list()
        
        if root is None:
            return nodes
        
        if len(nodes) == lvl:
            nodes.append( [] )

        nodes[lvl].append(root.val)
        self.levelOrder(root.left, lvl+1, nodes)
        self.levelOrder(root.right, lvl+1, nodes)

        return nodes
    


class TestCase( unittest.TestCase ):
    def testCase1(self):
        root = TreeNode( 3, TreeNode(9), TreeNode( 20, TreeNode(15), TreeNode(17) ) )
        res = Solution().levelOrder(root).__str__()

        self.assertEqual(res, '[[3], [9, 20], [15, 17]]', f'{res}')


    def testCase2(self): 
        root = TreeNode(1)
        res = Solution().levelOrder(root).__str__()

        self.assertEqual(res, '[[1]]', f'{res}')



if __name__ == '__main__':
    unittest.main()