from typing import List

board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

#[board[4][3:]+board[5][3:]+board[6][3:]]
sqaure11=list([board[0][:3]+board[1][:3]+board[2][:3]])
sqaure12=list([board[0][3:6],board[1][3:6],board[2][3:6]])
sqaure13=list([board[0][6:9],board[1][6:9],board[2][6:9]])

square1=list([board[0][:3]+board[1][:3]+board[2][:3]]+[board[0][3:6]+board[1][3:6]+board[2][3:6]]+[board[0][6:9]+board[1][6:9]+board[2][6:9]])

sqaure21=list([board[3][:3],board[4][:3],board[5][:3]])
sqaure22=list([board[3][3:6],board[4][3:6],board[5][3:6]])
sqaure23=list([board[3][6:9],board[4][6:9],board[5][6:9]])

sqaure31=list([board[6][:3],board[7][:3],board[8][:3]])
sqaure32=list([board[6][3:6],board[7][3:6],board[8][3:6]])
sqaure33=list([board[6][6:9],board[7][6:9],board[8][6:9]])

pivotBoard=list(zip(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))



print(sqaure31)
