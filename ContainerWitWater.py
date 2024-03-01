from typing import List
class Solution:
    def maxArea1(self, height: List[int]) -> int:
        
        i =0
        j= len(height)-1
        fg= lambda h,minX,maxX: maxX if h[maxX]> h[minX]+maxX else minX
        fl= lambda h,minX,maxX: maxX if h[maxX]> h[minX]-maxX else minX
        if(i<j):
                        
            if(height[i]>height[j]):
                k=j-1

                while (k>i and i<j):
                    k=k-1
                    j=fl(height,k,j)
                
            else:
                l=i+1
                while(l<j and i<j):
                    l=l+1
                    i=fg(height,i,l)
              
            length= height[i] if height[i]>height[j] else height[j]
            breadth=j-i                        
      
        return length*breadth
    
    
    def maxArea(self, height: List[int]) -> int:
        
        i=0
        j=len(height)-1  
        area=0
        while(i!=j):
            length= height[i] if height[i]<height[j] else height[j]
            breadth=j-i
            a1=length*breadth
            area= a1 if a1>area else area 
            
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
            
                       
      
        return area
    
    
    
obj=Solution()
height = [1,8,6,2,5,4,8,3,7]
#height=[1,2,1]
height=[1,1]
print("Area is",obj.maxArea(height))