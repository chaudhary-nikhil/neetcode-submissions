class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        rows = len(matrix)
        cols = len(matrix[0])
        r = (rows * cols) - 1

        while(l <= r):
            m = (int) ((l + r)/2)
            a = (int) (m / cols)
            b = (int) (m % cols)

            print(l)
            print(r)
            print(matrix[a][b])

            if(matrix[a][b]==target):
                return True
            elif(matrix[a][b] < target):
                l = m + 1
            else:
                r = m - 1
        
        return False
