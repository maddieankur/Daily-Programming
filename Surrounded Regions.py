"""
130. Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.



"""


class Solution(object):
    def isValid(self,a,b,n,m):
        #print(a,b,n,m)
        if 0<=a and a<n and 0<=b and b<m:
            return True
        return False
            
    def bfs(self,sX,sY,n,m,board,visited):
        #print(sX,sY)
        visited[sX][sY] = True
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            if self.isValid(sX+dx[i],sY+dy[i],n,m) and board[sX+dx[i]][sY+dy[i]] == 'O' and visited[sX+dx[i]][sY+dy[i]] == False:
                self.bfs(sX+dx[i],sY+dy[i],n,m,board,visited)
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """ 
        if board == []:
            return []
        n = len(board)
        m = len(board[0])
        impossible = [[False]*m for _ in range(n)]
        visited = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1)  or (j==0 or j ==m-1):
                    if visited[i][j] == False and board[i][j] == 'O':
                        self.bfs(i,j,n,m,board,visited)
        for i in range(0,n):
            for j in range(0,m):
                if visited[i][j] == True:
                    continue
                else:
                    board[i][j] = 'X'
        
