from typing import List, Counter

class Solution:
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
