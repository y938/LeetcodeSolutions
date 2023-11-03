# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        stk = []
        last = None
        for num in nums:
            while stk and stk[-1].val<num:
                last = stk.pop()
            node = TreeNode(num)
            if last:
                node.left = last
            if stk:
                stk[-1].right = node
            stk.append(node)
            last=None
        return stk[0]