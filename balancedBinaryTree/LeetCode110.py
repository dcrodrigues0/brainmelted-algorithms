# Definition for a binary tree node.

from typing import Optional

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root is None:
                return [True, 0] # true means that there is no more to traverse, and 0 means that achieve the most depht node in

            right = dfs(root.right) # Traversing the nodes in right
            left = dfs(root.left) # Traversing the nodes in left

            balanced = (right[0] and left[0] and #Verifying if i'm in the most depth node at right and left
                (abs(right[1] - left[1]) <= 1)) #verifying the difference between right depth and left depth
            
            return [balanced, 1 + max(right[1], left[1])]

        return dfs(root)[0]    
