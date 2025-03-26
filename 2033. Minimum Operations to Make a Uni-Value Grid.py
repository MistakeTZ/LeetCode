class Solution(object):
    def minOperations(self, grid, x):
        reference = grid[0][0] % x
        n, m = len(grid), len(grid[0])
        divs = [0] * (n * m)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] % x != reference:
                    return -1
                divs[i * m + j] = grid[i][j] // x
        
        avg = round(sum(divs) / (n * m))
        count = 0
        for i in range(n):
            for j in range(m):
                count += abs(divs[i * m + j] - avg)
        return count


print(Solution().minOperations(grid = [[2,4],[6,8]], x = 2))
print(Solution().minOperations(grid = [[1,5],[2,3]], x = 1))
print(Solution().minOperations(grid = [[1,2],[3,4]], x = 2))
print(Solution().minOperations(grid = [[931,128],[639,712]], x = 73))