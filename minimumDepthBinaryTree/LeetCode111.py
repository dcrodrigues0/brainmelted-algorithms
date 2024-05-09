#  Leet Code 111. Minimum Depth of Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return root

        def dfs(root):
            if root is None:
                return 0
            
            right = dfs(root.right)
            left = dfs(root.left)

            return 1 + max(right, left)
        
        return dfs(root)