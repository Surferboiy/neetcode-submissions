class Solution:
    def reorderList(self,head:Optional[ListNode])->None:
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow.next
        slow.next=None
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        while(prev):
            temp1=head.next
            temp2=prev.next
            head.next=prev
            prev.next=temp1
            head=temp1
            prev=temp2


        

        
        
        