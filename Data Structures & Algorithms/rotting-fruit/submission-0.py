class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 2):
                    q.append((i, j, 0))

        maxMin = 0

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            a, b, minutes = q.popleft()
            
            for da, db in directions:
                i = a + da
                j = b + db
                if(i >= 0 and i < rows and j >= 0 and j < cols and grid[i][j] == 1):
                    # update grid to rotten
                    grid[i][j] = 2
                    # append to queue
                    q.append((i,j, minutes + 1))
                    if(minutes + 1) > maxMin:
                        maxMin = minutes +1
        
        for i in range( rows):
            for j in range(cols):
                if(grid[i][j] == 1):
                    return -1
        

        

        print(grid)
        return maxMin