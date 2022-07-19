class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # capture all 'islands' that are 4-directionally surrounded by X`
        # flip the island in-place

        # when to flip:
        # - when entire island is surrounded by Xs
        # => how to know if an island is indexaed an island?

        # reverse DFS: traverse from the borders
        # if there is any 'island' that can reach the 'border', then it is                 #not counted as a surrounded island
        # our only job is to mark them all as "E" or "edge", the rests are the
        # islands we need to flip

        row_len = len(board)
        col_len = len(board[0])

        def dfs(r, c, board):
            if r < 0 or r == row_len or c < 0 or c == col_len:
                return
            if board[r][c] == 'O':
                board[r][c] = 'E'
                dfs(r + 1, c, board)
                dfs(r - 1, c, board)
                dfs(r, c + 1, board)
                dfs(r, c - 1, board)

        for r in range(row_len):
            dfs(r, 0, board)
            dfs(r, col_len - 1, board)

        for c in range(col_len):
            dfs(0, c, board)
            dfs(row_len - 1, c, board)

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'E':
                    board[r][c] = 'O'


