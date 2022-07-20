class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # m x n grid rooms, three possible values
        # -1: wall or obstacles
        # 0: gate
        # INF: empty room

        # fill each empty room with the distance to the nearest gate, if impossible then -1
        # we can actually BFS backwards from the gates itselves
        EMPTY = 2 ** 31 - 1
        row_len, col_len = len(rooms), len(rooms[0])
        queue = deque()
        visited = set()

        for r in range(row_len):
            for c in range(col_len):
                if rooms[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = dist
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or row == row_len or col < 0 or col == col_len or (row, col) in visited or rooms[row][
                        col] != EMPTY:
                        continue
                    visited.add((row, col))
                    queue.append([row, col])
            dist += 1

        # return(rooms)







