"""
69. x的平方根
"""
class Solution_69:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        if x == 1 or x == 0:
            return x
        while (left < right):
            mid = left + (right - left) / 2
            if (mid * mid < x):
                left = mid + 1
            elif (mid * mid > x):
                right = mid
            else:
                return mid
        return right