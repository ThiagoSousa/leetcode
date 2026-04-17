class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0)+1
        for c in ransomNote:
            if c not in d or d[c] <=0:
                return False
            else:
                d[c] -= 1
        return True