# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        x = []
        x += self.inorderTraversal(root.left)  # Add left subtree results
        x.append(root.val)  # Add current node value
        x += self.inorderTraversal(root.right)  # Add right subtree results
        return x
