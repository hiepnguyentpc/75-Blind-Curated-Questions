class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # mxn matrix with heights[r][c] is the height about sea level at [r][c]
        # if the neighboring cell's height is <= current cell height
        # return 2D list of grid coordinates results[i]
        # result[i] = [r_i, c_i] where rain water can flow from [r][c] to BOTH Pacific and Atlantic Ocean

        # brute force solution: check every cell to see if it can reach to PO or AO
        # optimized: DFS backwards from the PO and AO

        row_len = len(heights)
        col_len = len(heights[0])
        pacific = set()
        atlantic = set()

        def DFS(r, c, visited, prevHeight):
            # base case
            if (r, c) in visited or r < 0 or r == row_len or c < 0 or c == col_len or heights[r][c] < prevHeight:
                return
            # the important/meat here is the list visited
            visited.add((r, c))
            DFS(r - 1, c, visited, heights[r][c])
            DFS(r + 1, c, visited, heights[r][c])
            DFS(r, c + 1, visited, heights[r][c])
            DFS(r, c - 1, visited, heights[r][c])

        for r in range(row_len):
            DFS(r, 0, pacific, heights[r][0])
            DFS(r, col_len - 1, atlantic, heights[r][col_len - 1])

        for c in range(col_len):
            DFS(0, c, pacific, heights[0][c])
            DFS(row_len - 1, c, atlantic, heights[row_len - 1][c])

        res = []
        for r in range(row_len):
            for c in range(col_len):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res

