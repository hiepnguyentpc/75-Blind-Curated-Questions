class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # search for value 'target' in an mxn matrix
        # integers sorted from left to right
        # first integer of each row is greater than the last integer of the previous row

        row_len, col_len = len(matrix), len(matrix[0])

        # brute force - accepted

        # for r in range(row_len):
        #    for c in range(col_len):
        #        if matrix[r][c] == target:
        #            return True
        # return False

        # binary search

        left, right = 0, row_len * col_len - 1
        while left <= right:
            pivot = (left + right) // 2
            pivot_element = matrix[pivot // col_len][pivot % col_len]

            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot - 1
                else:
                    left = pivot + 1
        return False