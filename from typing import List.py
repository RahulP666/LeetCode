from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minVal=min(prices)
        minIndex=prices.index(minVal)
        
        priceNew=prices[minIndex:]
        maxVal=max(priceNew)
        
        if maxVal>minVal:
            return maxVal-minVal
        
        return 0
    
    
    
obj=Solution()
    
prices = [7,1,5,3,6,4]
  
print("result is ",obj.maxProfit(prices))