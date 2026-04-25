# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            print(f"prev: {prev.val if prev else None} curr: {curr.val} next: {next.val if next else None}")
            curr.next = prev
            prev = curr
            curr = next
            print(f"prev: {prev.val if prev else None} curr: {curr.val if curr else None} next: {next.val if next else None}")
            
        return prev

            