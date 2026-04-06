# Linked List Problems

This file is reserved for linked list-related problem notes, solutions, and references.

## Section Links

- Notion Linked List Notes: 

## Basic Linked List Operations

### Insert

```python
temp.next = newNode
```


### Delete

```python
temp.next = temp.next.next
```

### Insert/Delete at pos

```python
#to delete at pos, we have to reach pos-1
#to reach pos-1, we have to traverse pos-2 as head already at pos1
for _ in range(1,pos-1):
    head=  head.next
```

## DLL Basic Operations

### Insert

- Start/End/Random/After/Before → 4 node change (2 newnode and opposite connection to those 2)

```python
# insert new_node between left and right
new_node.prev = left
new_node.next = right
left.next = new_node
right.prev = new_node
```

### Delete

- at Start/End/Random/After/Before → ignore the delete node

```python
temp.prev.next = temp.next.prev
```

## Linked List Problem Solving

### Patterns

- Two Pointers (slow/fast): Use slow and fast pointers to find middle, detect cycles, or find nth node from end.
- Slow and Fast Pointer (finding middle):
    1. 1st mid -> s = head, f = head.next
    2. 2nd mid -> s = f = head
- Dummy Node: Prepend a dummy node to simplify edge cases involving head deletion or insertion.
- Reverse in Place: Use prev/cur/nxt pointers to reverse links iteratively without extra space.
- Merge: Merge two sorted lists by comparing heads and linking the smaller node first.
- Cycle Detection: Floyd's algorithm — if slow and fast ever meet, a cycle exists.

### Problem Tracker

| S.No | Problem Name | Hint | Solution Link | Reference |
|---|---|---|---|---|
| 1 | [Delete a Node in Single Linked List](https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1) | Traverse to node x-1 and bypass xth node | [Python](../code/delete_node_single_linked_list.py) |  |
| 2 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Keep fast pointer n steps ahead, then move both to find node before target | [Python](../code/remove_nth_node_from_end_of_list.py) |  |
| 3 | [Reverse a Doubly Linked List](https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1) | Swap prev and next for each node; the last processed node becomes the new head | [Python](../code/reverse_doubly_linked_list.py) |  |
| 4 | [Find the First Node of Loop in Linked List](https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1) | Floyd detect cycle, then reset slow to head and move both by 1 to find loop start | [Python](../code/find_first_node_of_loop.py) | [Reference](https://stackoverflow.com/questions/36696584/detect-first-node-in-the-cycle-in-linked-list) |

