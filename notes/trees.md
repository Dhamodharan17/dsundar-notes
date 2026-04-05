# Tree Problems

This file is reserved for tree-related problem notes, solutions, and references.

## Section Links

- Notion Tree Notes: https://www.notion.so/2deab1fe3aaa800181fecf300a276d93?v=2deab1fe3aaa80b0a0d9000c1d73205d

## Tree Traversal

### DFS Preorder (DLR)

Practice link: https://practice.geeksforgeeks.org/problems/preorder-traversal/1

<details>
<summary>Show/Hide Preorder Code</summary>

```python
class Solution:
	#DLR
	def preOrder(self, root):
		res =[]
		def f(node):
			if not node:
				return
			res.append(node.data)
			f(node.left)
			f(node.right)
		f(root)
		return res
```

</details>

### Level Order Traversal (BFS)

Practice link: https://leetcode.com/problems/binary-tree-level-order-traversal/

<details>
<summary>Show/Hide Level Order Code</summary>

```python
class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

		res = []
		if not root:
			return []

		q = deque([root])

		while q:
			size = len(q)
			temp = []
            '''We freeze the current level size first; this prevents next-level (enqueued now) nodes from being processed in the same level.'''
			for _ in range(size):
				cur = q.popleft()
				temp.append(cur.val)
				if cur.left:
					q.append(cur.left)
				if cur.right:
					q.append(cur.right)
			res.append(list(temp))

		return res
```

</details>

## Basic Tree operation

### Insert and Delete (Pointer Update Basics)

In a binary tree, basic insert and delete actions are done by updating child pointers.

Insert:

```python
node.left = newNode
# or
node.right = newNode
```

Delete (detach or ignore that child node from the current tree):

```python
node.left = None
# or
node.right = None
```

Note: Setting a child to `None` disconnects that node from this tree path. If that node has children, its subtree is also detached from this parent link.

### BST Insert

Practice link: https://www.geeksforgeeks.org/problems/insert-a-node-in-a-bst/1

<details>
<summary>Show/Hide BST Insert Code</summary>

```python
class Solution:
	def insert(self, root, key):

		if not root:
			return Node(key)
		#key greater than current - should go right
		if key >= root.data:
			root.right = self.insert(root.right, key)
		else:
			root.left = self.insert(root.left, key)

		return root
```

</details>

### BST Delete

Practice link: https://www.geeksforgeeks.org/problems/delete-a-node-from-bst/1

<details>
<summary>Show/Hide BST Delete Code</summary>

```python
class Solution:
	def delNode(self, root, x):

		def fetchInorder(node):
			while node and node.right:
				node = node.right
			return node

		def handleDelete(node):
			if not node.left and not node.right:
				return None
			if not node.left:
				return node.right
			if not node.right:
				return node.left

			inorder = fetchInorder(node.left)
            #replace the delete node
			node.data = inorder.data
            #as we took the node from left, delete on the left tree
			node.left = find(node.left, inorder.data)
			return node

		def find(node, key):
			if not node:
				return None
			if node.data == key:
				return handleDelete(node)
			if key > node.data:
				node.right = find(node.right, key)
			else:
				node.left = find(node.left, key)
			return node

		return find(root, x)
```

</details>

## Tree Problems Solving

### Patterns

- Preorder: Process the current node first, then go to the left child and the right child.
- Postorder: First process the left child and right child, then process the current node.
- Inorder: First process the left child, then the current node, then the right child.
- Level Order Traversal: Process nodes level by level from left to right, usually using a queue.

### Problem Tracker

| S.No | Problem Name | Hint | Solution Link | Image |
|---|---|---|---|---|
| 1 | [Same Tree](https://leetcode.com/problems/same-tree/) | if not p or not q - check value and structural equivalence |  |  |
| 2 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | 1 + max(f(x.left), f(x.right)) - each subtree retuns max path |  |  |
| 3 | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | use deque and appendleft to avoid reversing |  |  |
| 4 | [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | every node from target - return +1 | [Code](../code/distance_k_binary_tree.py) |  |
| 5 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | postorder; keep global ans with node+left+right and return node+max(left,right); ignore -ve using max(0, left) |  |  |
| 6 | [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | dfs with (row,col), group by col then row, sort values for ties | [Code](../code/vertical_traversal.py) |  |
| 7 | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | move left subtree to right, walk to new right tail, then attach saved right subtree | [Code](../code/flatten_binary_tree_linked_list.py) |  |
| 8 | [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/) | postorder last element is root; leftNodes = rootIndex - iStart | [Code](../code/construct_tree_inorder_postorder.py) | [Image](../images/constructbt.png) |
| 9 | [Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/description/) | level-order traversal; keep (node, parent) in queue | [Code](../code/cousins_in_binary_tree.py) |  |

