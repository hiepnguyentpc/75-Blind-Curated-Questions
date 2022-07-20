class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

        # Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

        # since it's mininum number of minutes, the intuition would be using BFS

        row_len = len(grid)
        col_len = len(grid[0])
        time, fresh = 0, 0
        queue = deque()
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue and fresh > 0:

            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == row_len or col < 0 or col == col_len or
                            grid[row][col] != 1):
                        continue  # break out of loop
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
















