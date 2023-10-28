class Solution:
    """
    27. 移除元素
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
        return slow