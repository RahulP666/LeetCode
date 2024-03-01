# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def ConvertListtoLinkedList(self, lst=[])-> ListNode:
        
        l=None
        for i in reversed(lst) :
            if l==None:
                l=ListNode(val=i)
            else:
                l1=ListNode(val=i,next=l)
                l=l1
                
                
            
        return l

        
    def addTwoNumbers(self, lst1: Optional[ListNode], lst2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        carry=0
        lst3=[]
        
        #l1=self.ConvertListtoLinkedList(lst=lst1)
        #l2=self.ConvertListtoLinkedList(lst=lst2)
        l1=lst1
        l2=lst2
        while l1!= None or l2!= None:
            
            a= 0 if l1 == None else l1.val
            b= 0 if l2 == None else l2.val
            total= a+b+carry
            #print(a,"+",b,"=",total," sum")
            sum = total%10
            carry= int(total/10)
            #print(a,"+",b,"=",total," sum", sum)
            lst3.append(sum)
            if(l1!=None):
                l1=l1.next 
            if(l2!=None):
                l2=l2.next
        
        if carry>0:
            lst3.append(carry)
        l3=self.ConvertListtoLinkedList(lst3)

        
        return l3
    

l13=[0]
l23=[0]

obj=Solution()
l3=obj.addTwoNumbers(lst1=l13 ,lst2=l23)

print("Wow")

    
    


    
    
        