from typing import List, DefaultDict

class Solution:
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

