# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        t = [] #tree
        s = [] # subtree


        def dfs1(node):
            if not node:
                t.append("#")
                return
            t.append(node.val)    
            dfs1(node.left)
            dfs1(node.right)

        def dfs2(node):
            if not node:
                s.append("#")
                return
            s.append(node.val)
            dfs2(node.left)
            dfs2(node.right)  

        dfs1(root)
        dfs2(subRoot) 
        s = ",".join(str(x) for x in s)
        t = ",".join(str(x) for x in t)

        return s in t    
        

