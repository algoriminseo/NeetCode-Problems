# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.height(root) != -1)


    def height(self, root):
        if not root:
            return 0 

        left, right = self.height(root.left), self.height(root.right)
        if left < 0 or right < 0:
            return -1
        
        if abs(right - left) > 1:
            return -1 
        
        return 1 + max(left, right)





