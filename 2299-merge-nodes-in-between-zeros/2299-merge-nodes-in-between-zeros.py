# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = []
        while head:
            x.append(head.val)
            head = head.next
        y = []
        z = []
        for i in x:
            if i==0 and i in y:
                z.append(sum(y))
                y=[0]
            else:
                y.append(i)
        head = ListNode(0)
        tail = head
        i = 0
        while i<len(z):
            node = ListNode(z[i])
            tail.next = node
            tail = tail.next
            i+=1
        return head.next
