from typing import List
import copy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0
        p1=copy.copy(prices)
        while len(p1)>1:
            minVal=min(p1)
            minIndex=p1.index(minVal)
            priceNew=copy.copy(p1)
            while(minIndex==len(priceNew)-1 ):
                priceNew=priceNew[:minIndex]
                if (len(priceNew)<1):
                    return profit
                minVal=min(priceNew)
                minIndex=priceNew.index(minVal)
            
                
            priceNew= priceNew[minIndex:]   #prices[minIndex:] if not flag else priceNew
            maxVal=max(priceNew)
            
            if maxVal>minVal and maxVal-minVal>profit :
                profit= maxVal-minVal
            
            p1=p1[:minIndex]
            priceNew=copy.copy(p1)
                
            
        
        return profit
    
    
    
obj=Solution()
    
#prices = [3,2,6,5,0,3]
prices=[4,2,1,7]
print("result is ",obj.maxProfit(prices))