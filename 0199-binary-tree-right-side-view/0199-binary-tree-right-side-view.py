# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# No/Yes left, right exists, right will be seen
# left exists, No right, left will be seen
# No left, No right, nothing will be seen 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res