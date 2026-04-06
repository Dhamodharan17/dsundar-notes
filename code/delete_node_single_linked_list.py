class Solution:
    def deleteNode(self, head, x):

        if x == 1:
            return head.next

        temp = head
        # reach x-1
        for _ in range(1, x - 1):
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
        return head
