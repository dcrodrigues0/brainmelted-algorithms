# LeetCode 226. Invert Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        def dfs(root):
            if root is None:
                return
            
            dfs(root.right)
            dfs(root.left)
            root.right,root.left = root.left, root.right

        dfs(root)
        return root
            
#This solution offers runtime 27ms 