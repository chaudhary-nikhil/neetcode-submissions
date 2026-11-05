class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        ans = 0

        cols = len(grid[0])
        rows = len(grid)

        for i in range(rows):
            for j in range (cols):
                if(grid[i][j] == '1'):
                    q.append((i, j, 0))

        while(q):
            a, b, land = q.pop()
            if(a >= 0 and a < rows and b >= 0 and b < cols and grid[a][b] == '1'):
                ans += (not land)
                # you have a starting island
                # DFS
                grid[a][b] = '0' 
                q.append((a + 1, b, 1))
                q.append((a, b + 1, 1))
                q.append((a - 1, b, 1))
                q.append((a, b-1, 1))

        print(q)

        return ans
    
