class Solution:
    def reverse(self, head):
        temp = head
        while temp:
            nxt = temp.next
            # pull prev forward
            temp.next = temp.prev
            # push next backward
            temp.prev = nxt
            # above touched only current node pointers
            if not nxt:
                # because below code will make temp null
                return temp
            temp = nxt

        return temp
