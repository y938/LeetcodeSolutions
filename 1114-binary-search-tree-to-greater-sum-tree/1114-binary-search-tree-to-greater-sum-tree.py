# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur_sum=0
        def dfs(node):
            nonlocal cur_sum
            if node is None:
                return
            dfs(node.right)
            tp = node.val
            node.val+=cur_sum
            cur_sum += tp
            dfs(node.left)
        dfs(root)
        return root