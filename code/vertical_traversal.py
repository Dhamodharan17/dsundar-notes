from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # defaultdict keeps insertion order; row order is sorted explicitly below.
        col_map = defaultdict(lambda: defaultdict(list))
        self.min_col = float("inf")
        self.max_col = float("-inf")

        def traverse(node: Optional[TreeNode], col: int, row: int) -> None:
            if not node:
                return

            self.min_col = min(self.min_col, col)
            self.max_col = max(self.max_col, col)

            col_map[col][row].append(node.val)

            traverse(node.left, col - 1, row + 1)
            traverse(node.right, col + 1, row + 1)

        traverse(root, 0, 0)

        result = []
        # Take each column one by one.
        for c in range(int(self.min_col), int(self.max_col) + 1):
            temp = []
            # Ensure rows are processed in sorted order.
            sorted_row = sorted(col_map[c].keys())
            for r in sorted_row:
                temp.extend(sorted(col_map[c][r]))
            result.append(temp)

        return result
