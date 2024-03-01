class Solution:
    def TranslateRoman(self,c: str) -> int:
        IntTrans={
                    'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000
                }
        
        return IntTrans[c]
        
    
    def romanToInt(self, s: str) -> int:
        val=0
        t2=0
        for char in reversed(s):
            t1=self.TranslateRoman(char)
            
            #operate=lambda x,y,z: z-x if x<y else z+y 
            
            #val1=operate(x=t1,y=t2,z=val)
            #val=val1
            if t1<t2:
             val=val-t1
            else:
             val=val+t1
                        
            t2=t1
        
        return val
    

obj=Solution()

s="MCMXCIV"
print("number is ",obj.romanToInt(s))