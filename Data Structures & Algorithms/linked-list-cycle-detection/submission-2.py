# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        check=set()
        while(curr):
            if curr ==None:
                return False
            elif curr in check:
                return True
            else:
                check.add(curr)
            curr=curr.next
        return False
        