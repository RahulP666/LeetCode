
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        getArray=lambda a,b,c,d,target: [a,b,c,d] if a+b==target-c-d else None
        result=[]
        i=0
        
        length=len(nums)
        sortNums=sorted(nums)
        while i<(length-3):
            j=i+1
            while(j<(length-2)):
                print(i,",",j,"-",sortNums[i],sortNums[j],sortNums[j+1],sortNums[j+2])
                l1= getArray(sortNums[i],sortNums[j],sortNums[j+1],sortNums[j+2],target=target)
                
                if l1 != None and l1 not in result:
                    result.append(l1)
                j=j+1
            i=i+1
        
        return result
    

nums =[1,0,-1,0,-2,2]
target=0 
obj=Solution()
ln=obj.fourSum(nums,target)
ln
        