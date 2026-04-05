from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        while root:
            tempright = root.right
            root.right = root.left
            root.left = None

            # Even if root.left is None, start from root so the saved right subtree
            # can still be reattached to the current chain.
            t2 = root
            while t2 and t2.right:
                t2 = t2.right

            t2.right = tempright
            root = root.right
