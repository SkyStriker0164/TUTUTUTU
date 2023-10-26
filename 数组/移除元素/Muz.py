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
     
    

    """
    844. 比较含退格的字符串
    """

    """
    input: s = 'ab#c', t = 'ad#c'
    output: true
    explanation: both s and t become "ac".

    使用双指针模拟两个字符串退格
    """
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compare(s_obj: str) -> str:
            slow = 0
            s_obj = list(s_obj)
            for i in range(len(s_obj)):
                if s_obj[i] != '#':
                    s_obj[slow] = s_obj[i]
                    slow += 1
                else:
                    if slow > 0:
                        slow -= 1
            return s_obj[:slow]
        print(compare(s))
        print(compare(t))
        return compare(s) == compare(t)





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





if __name__ == "__main__": 
   s = Solution()
   print(s.backspaceCompare("a#c", "b"))
#    print(s.sortedSquares([-4, -1, 0, 2, 3]))
    