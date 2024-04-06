# LeetCode 111. Minimum depth of Binary Tree

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node):
            if node is None:
                return float('inf')

            if node.left is None and node.right is None:
                return 1

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            return min(left_depth, right_depth) + 1

        return dfs(root)
