class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        matrix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        matrix[0][0] = grid[0][0]

        for i in range(1, len(grid)):
            matrix[i][0] = matrix[i-1][0] + grid[i][0]

        for i in range(1, len(grid[0])):
            print(i)
            matrix[0][i] = matrix[0][i-1] + grid[0][i]



        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                matrix[i][j] = grid[i][j] + min(matrix[i-1][j], matrix[i][j-1])

        print(matrix)
        return matrix[-1][-1]