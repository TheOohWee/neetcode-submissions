# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        r1 = []
        r2 = []

        def dfs1(node):
            if not node:
                r1.append("#")
                return 
            dfs1(node.left)
            dfs1(node.right)
            r1.append(node.val)
        
        def dfs2(node):
            if not node:
                r2.append("#")
                return 
            dfs2(node.left)
            dfs2(node.right)
            r2.append(node.val) 

        dfs1(p)
        dfs2(q)       

        return r1 == r2