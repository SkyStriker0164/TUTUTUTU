"""
367. 有效的完全平方数
"""

class Solution_367:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        if num == 1:
            return True
        while (left < right):
            mid = left + (right - left) // 2
            if (mid * mid < num):
                left = mid + 1
            elif (mid * mid > num):
                right = mid
            else:
                return True
        return False
