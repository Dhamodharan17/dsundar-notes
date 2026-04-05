from collections import deque
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        # Store (node, parent).
        q = deque([(root, None)])

        while q:
            size = len(q)
            x_parent = None
            y_parent = None

            for _ in range(size):
                node, parent = q.popleft()

                if node.val == x:
                    x_parent = parent
                elif node.val == y:
                    y_parent = parent

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            # If both found at same level, they are cousins only if parents differ.
            if x_parent and y_parent:
                return x_parent != y_parent

            # If only one found at this level, they cannot be cousins.
            if x_parent or y_parent:
                return False

        return False
