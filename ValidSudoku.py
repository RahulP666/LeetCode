
from typing import List
class Solution:
    
    def isRepeating(self,lstBoard:List) -> bool:
        isNotRepeating=lambda l: False if len(l)!= len(set(l)) else True
        char_to_remove="."
        remove_char_from_listr= lambda lst,char_to_remove:[x for x in lst if x!=char_to_remove]
        r1= remove_char_from_listr (lstBoard,char_to_remove=char_to_remove)
        if not (isNotRepeating(l=r1)) :
            return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        
        j=0
        i=0
        #lambda multiList: self.isRepeating(lstBoard=[row for row in multiList])
        pivotBoard=list(zip(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))
        
        
        
        for rows in pivotBoard:
            if not self.isRepeating(lstBoard=rows):
                return False
            
        
        for rows in board:
            if not self.isRepeating(lstBoard=rows):
                return False
                
                        
        
        i=0
        square=[]
        while (i<9):
           square=square+[board[i][:3]+board[i+1][:3]+board[i+2][:3]]+[board[i][3:6]+board[i+1][3:6]+board[i+2][3:6]]+[board[i][6:9]+board[i+1][6:9]+board[i+2][6:9]]
           i=i+3
           
        for rows in square:
            if not self.isRepeating(lstBoard=rows):
                return False      
        
        return True
    
board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]    

obj=Solution()
t=obj.isValidSudoku(board=board)
print(t)

    