class Solution:
    def cycleStart(self, head):

        s = f = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if s == f:
                # loop detected
                s = head
                while s != f:
                    s = s.next
                    f = f.next
                return s.data
        return -1
