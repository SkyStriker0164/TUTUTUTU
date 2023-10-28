from typing import List
class Solution:
    """
    26. 删除排序数组中的重复项
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for i in range(0, len(nums)):
            if(nums[slow] == nums[i]):
                i += 1
            else:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1
    