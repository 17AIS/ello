# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        numbers = []

        curr = head
        i = 0
        start = head
        while curr and i < (right):
            if i == (left - 1):
                start = curr
            if i >= (left - 1):
                numbers.append(curr.val)
            curr = curr.next

            i += 1

        numbers.reverse()
        for i in numbers:
            if not start:
                break
            start.val = i
            start = start.next
        
        return head