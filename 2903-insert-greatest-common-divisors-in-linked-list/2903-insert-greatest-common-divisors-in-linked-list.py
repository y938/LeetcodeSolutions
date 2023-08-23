# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
            current = head
            while current is not None and current.next is not None:
                current.next = ListNode(gcd(current.val, current.next.val), next=current.next)
                current = current.next.next
            return head


