
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
    
