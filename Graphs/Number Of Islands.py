
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # matrix representation of undirected graph
        # island: surrounded by water, formed by connecting adjacent lands
        # all four edges of the grid are surrounded by water

        # idea: count how many times we can DFS inside graph, each time we DFS, we mark
        # the visited land as 0 (1->0)

        # DFS entire board, for whatever [i][j] == 1

        # the DFS on matrices is a little weird, since it's much easier to use recursion
        # than to use DFS with regular stack

        if len(grid) < 1:
            return 0
        row_len = len(grid)
        col_len = len(grid[0])
        islands = 0
        # Iterate through each row and colummn
        for r in range(0, row_len):
            for c in range(0, col_len):
                if grid[r][c] == '1':
                    # Call DFS when 1 is found
                    self.find(r, c, grid)
                    islands += 1
        return islands

    def find(self, r, c, grid):
        # Base Case - Stop recursion when out of bound
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] == '1':
            grid[r][c] = 0
            self.find(r - 1, c, grid)  # go up
            self.find(r + 1, c, grid)  # go down
            self.find(r, c + 1, grid)  # go right
            self.find(r, c - 1, grid)  # go left

