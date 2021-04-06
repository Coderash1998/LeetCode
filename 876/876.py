# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        c=0
        n=head
        while n:
            c+=1
            n=n.next
        n=head
        for _ in range(c//2):
            n=n.next
        return n