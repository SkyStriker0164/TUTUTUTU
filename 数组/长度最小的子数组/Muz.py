from typing import List, Counter, DefaultDict

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        cur_sum = 0
        i = 0
        for j in range(len(nums)):
            cur_sum += nums[j]
            while (cur_sum >= target):
                min_len = min(min_len, j - i + 1)
                cur_sum -= nums[i]
                i += 1
        return min_len if min_len != float('inf') else 0
    
    def totalFruit(self, fruits: List[int]) -> int:
        """
        纯set去重超时了
        """
        max_len = float('-inf')
        cur_len = 0
        i = 0
        for j in range(len(fruits)):
            cur_len = len(set(fruits[i:j+1]))
            if cur_len == 2:
                max_len = max(max_len, j - i + 1)
            while(cur_len > 2):
                i += 1
                cur_len = len(set(fruits[i:j+1]))
        return max(max_len, j - i + 1)
    
    def totalFruit_counter(self, fruits: List[int]) -> int:
        """
        这里用哈希表的方法
        """
        cnt = Counter()
        max_len = float('-inf')
        i = 0
        for j in range(len(fruits)):
            cnt[fruits[j]] += 1
            while (len(cnt) > 2):
                cnt[fruits[i]] -= 1
                if cnt[fruits[i]] == 0:
                    cnt.pop(fruits[i])
                i += 1
            max_len = max(max_len, j - i + 1)
        return max_len

    
    def minWindow(self, s: str, t: str) -> str:
        """
        维护need字典，还是通过滑动窗口的思想去解，mcdull解法
        """
        need = DefaultDict(int)
        for item in t:
            need[item] += 1
        needCnt = len(t)
        i = 0
        res = ''
        for j in range(len(s)):
            if s[j] in need:
                if need[s[j]] > 0:
                    needCnt -= 1
                need[s[j]] -= 1
            while(needCnt == 0):
                if not res or j - i + 1 < len(res):
                    res = s[i : j + 1]    
                if s[i] in need:
                    if need[s[i]] == 0:
                        needCnt += 1
                    need[s[i]] += 1
                i += 1
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC","ABC"))