from typing import List

class Solution:
    """
    977. 有序数组的平方
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        解法1：直接用内置函数怼
        """
        # return sorted([i**2 for i in nums])
        """
        解法2：双指针法，力扣上的解法是空间换时间，建一个新数组作快排
        """
        res = [-1] * len(nums)
        pos = len(nums) - 1
        for i in range(0, len(nums)):
            nums[i] = nums[i] ** 2
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                res[pos] = nums[right]
                right -= 1
            elif nums[left] >= nums[right]:
                res[pos] = nums[left]
                left += 1
            pos -= 1
        return res