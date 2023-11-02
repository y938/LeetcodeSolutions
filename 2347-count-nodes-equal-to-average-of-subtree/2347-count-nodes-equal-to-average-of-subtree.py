# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if not node:
                return (0,0)
            left = dfs(node.left)
            right = dfs(node.right)
            nonlocal res
            totsum = left[0] + right[0] + node.val
            count = left[1] + right[1] + 1
            res +=(node.val == totsum//count)
            return (totsum,count)
        dfs(root)
        return res
        