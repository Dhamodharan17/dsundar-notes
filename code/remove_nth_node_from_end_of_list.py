from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional["ListNode"], n: int) -> Optional["ListNode"]:

        s = f = head
        # If gap is n-1, slow lands on the target node, not previous node.
        for _ in range(n):
            f = f.next
        if not f:
            return head.next
        while f and f.next:
            s = s.next
            f = f.next
        if s.next:
            s.next = s.next.next
        return head
