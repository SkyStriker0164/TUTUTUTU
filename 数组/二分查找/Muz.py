"""
如果题目中提到了无重复元素，可以考虑二分查找
关键在于，边界条件是否合理
"""

"""
704. 二分查找
"""
from typing import List

class Solution_704:
    # [left, right]情况
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left<=right):
            middle = left + (right - left) // 2
            if (nums[middle] > target):
                right = middle - 1
            elif(nums[middle] < target):
                left = middle + 1
            else:
                return middle
        return -1


"""
35. 搜索插入位置
"""
class Solution_35:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left<=right):
            middle = left + (right - left) // 2
            if (nums[middle] > target):
                right = middle - 1
            elif(nums[middle] < target):
                left = middle + 1
            else:
                return middle
        return right + 1


"""
34. 在排序数组中查找元素的第一个和最后一个位置
"""
class Solution_34:
    def searchRange(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        firstIndex = -1
        lastIndex = -1
        while (left <= right):
            mid = left + (right - left) // 2 
            if nums[mid] == target:
                firstIndex = mid
                lastIndex = mid
                while firstIndex > 0 and nums[firstIndex - 1] == target:
                    firstIndex -= 1
                while lastIndex < len(nums) - 1 and nums[lastIndex + 1] == target:
                    lastIndex += 1
                return [firstIndex, lastIndex]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [firstIndex, lastIndex]
    

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
