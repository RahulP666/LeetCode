
class Solution:
    
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        hasDuplicate= lambda x: any ( x.count(y)>1 for  y in x )
        allDuplicate= lambda x: all ( x.count(y)>1 for  y in x )
        
        if  not s :
            return 0
        if not(hasDuplicate(s)):
            return len(s)
        
        #if (allDuplicate(s)):
        #    return 1
        
        i=0
        repStr=""
        while i<len(s):
            restStr=s[i+1:]
            if len(restStr)<len(repStr):
                break
            
            try:
                index=restStr.index(s[i])
            except:
                index=len(restStr)
            temp=s[i:index+i+1]
            print ("temp",temp)
            if not hasDuplicate(temp) and len(repStr)<len(temp):
                repStr=temp
                print(repStr)
            i=i+1
         
        
        return len(repStr)   
            



obj=Solution()

str1="cdd"
print(obj.lengthOfLongestSubstring(s= str1))
