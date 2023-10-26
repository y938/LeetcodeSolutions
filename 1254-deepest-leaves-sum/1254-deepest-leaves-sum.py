from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root,0))
        level = 0
        result = 0
        while q:
            cand, depth = q.popleft()
            if depth > level:
                result = 0
                level = depth
            if depth == level:
                result += cand.val
            if cand.left:
                q.append((cand.left, depth+1))
            if cand.right:
                q.append((cand.right, depth+1))
        return result