class Solution:
    def spiralOrder(self, matrix):
        result = []

        if not matrix:
            return []

        row1 = 0
        col1 = 0
        row2 = len(matrix) - 1
        col2 = len(matrix[0]) - 1

        def helper(row1, col1, row2, col2):
            # 两个矩阵的对角点就可以确定一个矩阵
            for c in range(col1, col2 + 1):
                result.append(matrix[row1][c])

            for r in range(row1 + 1, row2 + 1):
                result.append(matrix[r][col2])
            if row1 < row2 and col1 < col2:
                for c in range(col2 - 1, col1 - 1, -1):
                    result.append(matrix[row2][c])

                for r in range(row2 - 1, row1, -1):
                    result.append(matrix[r][col1])

        while row1 <= row2 and col1 <= col2:
            helper(row1, col1, row2, col2)
            row1 += 1
            row2 -= 1
            col1 += 1
            col2 -= 1
        return result

a = Solution()
print(a.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
