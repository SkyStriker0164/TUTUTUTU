from typing import List
class Solution:
    """
    283. 移动零
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            fast = i
            if nums[i] == 0:
                while True:
                    fast += 1
                    if fast == len(nums):
                        break
                    if nums[fast] != 0:
                        break
                if fast == len(nums):
                    break
                else:    
                    nums[i], nums[fast] = nums[fast], nums[i]
     