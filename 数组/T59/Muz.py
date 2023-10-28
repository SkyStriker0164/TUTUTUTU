from typing import List

class Solution:
    """
    左闭右开，按蛇形遍历
    1.右至左
    2.上至下
    3.左至右
    4.下至上
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        start_x = 0
        start_y = 0
        offset = 1 # 作为每次代码执行的偏移量
        cnt = 1
        mid = n // 2
        for offset in range(1, n // 2 + 1):
            for j in range(start_y, n - offset):
                nums[start_x][j] = cnt
                cnt += 1
            for i in range(start_x, n - offset):
                nums[i][n - offset] = cnt
                cnt += 1
            for j in range(n - offset, start_y, -1):
                nums[n - offset][j] = cnt
                cnt += 1
            for i in range(n - offset, start_x, -1):
                nums[i][start_y] = cnt
                cnt += 1
            
            start_x += 1
            start_y += 1
        if n % 2 != 0:
            nums[mid][mid] = cnt
        return nums


        



if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix())