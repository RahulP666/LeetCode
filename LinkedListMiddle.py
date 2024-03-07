from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        i=0
        
        ptr= head
        while (ptr.next != None):
            ptr=ptr.next
            i=i+1
            
        
        remainder= i%2
        half=i/2 if remainder == 0 else i/2+1
        
        j=0
        ptr2=head
        while (j<half):
         ptr2=ptr2.next
         j=j+1
        
        
        return ptr2
    
    
lst1=ListNode(val=5,next=None)
lst2=ListNode(val=4,next=lst1)
lst3=ListNode(val=3,next=lst2)
lst4=ListNode(val=2,next=lst3)
lst5=ListNode(val=1,next=lst4)
obj= Solution()
obj.middleNode(lst5)

    
    
