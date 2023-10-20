"""
移除元素这里提到一种很实用的解法，叫快慢指针法

快指针遍历所有元素，慢指针遍历非目标值元素

这样就对数据重新进行了覆盖
"""

from typing import List

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
    

    """
    283. 移动零
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for i in range(0, len(nums)):
            print(f"第{i+1}轮：{nums}")
            if slow == len(nums) - 1:
                break
            if nums[i] == 0:
                slow = i+1
                for j in range(slow, len(nums)):
                    if nums[j] != 0:
                        break
                    else:
                        slow = j
                nums[i], nums[slow] = nums[slow], nums[i]
        print(f"nums的值为{nums}")
    

    """
    844. 比较含退格的字符串
    """

    def backspaceCompare(self, s: str, t: str) -> bool:
        pass


    """
    977. 有序数组的平方
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pass





if __name__ == "__main__": 
   s = Solution()
   s.moveZeroes([0,1,0,3,12])
    