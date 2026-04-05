from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    #basic template
    def f(root, l, r):
        if not root:
            return None
        m = l+r//2
        root = TreeNode(m)
        root.left = f(root.left, l, m-1) if root.left else None
        root.right = f(root.right, m+1, r) if root.right else None
        return root
    

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def builtTree(pStart, pEnd, iStart, iEnd):
            if iStart > iEnd or pStart > pEnd:
                return None

            root = TreeNode(postorder[pEnd])
            rootIndex = 0
            for i in range(iStart, iEnd + 1):
                if inorder[i] == postorder[pEnd]:
                    rootIndex = i
                    break

            leftNodes = rootIndex - iStart
            #left half
            root.left = builtTree(pStart, pStart + leftNodes - 1, iStart, rootIndex - 1)
            #right half
            root.right = builtTree(pStart + leftNodes, pEnd - 1, rootIndex + 1, iEnd)

            return root

        return builtTree(0, len(postorder) - 1, 0, len(inorder) - 1)
