class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        k=0
        for i in range(8):
            for j in range(8):
                if  board[i][j]=='R':
                    r1,r2=i,j
                    break
        for i in range(r1-1,-1,-1):
            if board[i][r2]=='B':
                break
            if board[i][r2]=='p':
                k+=1
                break
        for i in range(r1+1,8):
            if board[i][r2]=='B':
                break
            if board[i][r2]=='p':
                k+=1
                break
        for i in range(r2-1,-1,-1):
            if board[r1][i]=='B':
                break
            if board[r1][i]=='p':
                k+=1
                break
        for i in range(r2+1,8):
            if board[r1][i]=='B':
                break
            if board[r1][i]=='p':
                k+=1
                break
        return k