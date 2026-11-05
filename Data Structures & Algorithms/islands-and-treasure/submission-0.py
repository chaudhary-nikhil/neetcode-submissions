class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        list = deque()

        rows = len(grid)
        cols = len(grid[0])

        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if(grid[i][j]==0):
                    list.append([i,j])

    
        while list:
            i, j = list.popleft()
            
            if(i+1<rows and j<cols and grid[i+1][j] == 2147483647):
                grid[i+1][j] = grid[i][j] + 1
                list.append((i+1,j))

            if(i<rows and j+1<cols and grid[i][j+1] == 2147483647):
                grid[i][j+1] = grid[i][j] + 1
                list.append((i,j+1))

            if(i-1<rows and i-1 >= 0 and j<cols and grid[i-1][j] == 2147483647):
                grid[i-1][j] = grid[i][j] + 1
                list.append((i-1,j))
        
            if(i<rows and j-1<cols and j-1 >= 0 and grid[i][j-1] == 2147483647):
                grid[i][j-1] = grid[i][j] + 1
                list.append((i,j-1))


        return       