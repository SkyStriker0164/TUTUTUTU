from typing import List

class Solution:
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