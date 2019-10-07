"""
200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input:
11110
11010
11000
00000

Output: 1
Example 2:
Input:
11000
11000
00100
00011

Output: 3



"""




class Solution:
    def isValid(self,a,b,n,m):
        if 0<=a and a<=n-1 and 0<=b and b<=m-1:
            return True
        return False
            
        
    def bfs(self,visited, grid,sX,sY,n,m):
        visited[sX][sY] = True
        conditionX=[-1,1,0,0]
        conditionY =[0,0,1,-1]
        for i in range(4):
            if self.isValid(sX+conditionX[i],sY+conditionY[i],n,m) and grid[sX+conditionX[i]][sY+conditionY[i]] == '1' and visited[sX+conditionX[i]][sY+conditionY[i]] == False :
                self.bfs(visited,grid,sX+conditionX[i],sY+conditionY[i],n,m)
        
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j] == False:
                    self.bfs(visited,grid,i,j,n,m)
                    ans+=1
        return ans
        
        
