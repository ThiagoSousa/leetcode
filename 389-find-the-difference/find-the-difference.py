class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_dict = {}
        for c in s:
            count_dict[c] = count_dict.get(c, 0)+1
        for c in t:
            if c not in count_dict:
                return c
            elif count_dict[c]==0:
                return c
            count_dict[c] -= 1