from typing import List


class Solution:
    """
    思路参考：https://cloud.tencent.com/developer/article/1606804
    """
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        if not array:
            return []
        left, right, top, bottom, ans = 0, len(array[0]) - 1, 0, len(array) - 1, []
        while True:
            for i in range(left, right + 1):
                ans.append(array[top][i])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom + 1):
                ans.append(array[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                ans.append(array[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                ans.append(array[i][left])
            left += 1
            if left > right:
                break
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.spiralArray([[2,3]]))
