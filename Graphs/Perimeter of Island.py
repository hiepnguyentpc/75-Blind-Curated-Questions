class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row_len = len(grid)
        col_len = len(grid[0])

        result = 0

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1:
                    # case 1: upper has an element
                    # case 2: lower has an element
                    # case 3: right has an element
                    # case 4: left has an element

                    # edge cases: cell in one of four corners

                    if r == 0:
                        up = 0
                    else:
                        up = grid[r - 1][c]

                    if c == 0:
                        left = 0
                    else:
                        left = grid[r][c - 1]

                    if r == row_len - 1:
                        down = 0
                    else:
                        down = grid[r + 1][c]

                    if c == col_len - 1:
                        right = 0
                    else:
                        right = grid[r][c + 1]

                    result += 4 - (up + down + left + right)

        return result










