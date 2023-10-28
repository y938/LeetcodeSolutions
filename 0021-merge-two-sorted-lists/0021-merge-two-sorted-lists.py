# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            
            x = []
            while list1 or list2:
                if list1:
                    x.append(list1.val)
                    list1 = list1.next
                else: 
                    x.append(list2.val)
                    list2 = list2.next
            x.sort()
            head = ListNode(0)
            tail = head
            for i in range(len(x)):
                node = ListNode(x[i])
                head.next = node
                head = node
                
            return tail.next
