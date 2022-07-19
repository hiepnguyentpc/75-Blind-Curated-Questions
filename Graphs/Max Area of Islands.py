class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for r in range(row_len):
            for c in range(col_len):
                max_area = max(max_area, self.getAreaOfIsland(r, c, grid))
        return max_area

    def getAreaOfIsland(self, r, c, grid):
        # base case
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 0

        if grid[r][c] == 1:
            grid[r][c] = 0
            return 1 + (self.getAreaOfIsland(r - 1, c, grid) + self.getAreaOfIsland(r + 1, c, grid)
                        + self.getAreaOfIsland(r, c - 1, grid) + self.getAreaOfIsland(r, c + 1, grid))
        return 0