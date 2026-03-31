class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle)>len(haystack):
            return -1
        
        for i in range(len(haystack)):
            found = True
            for j in range(len(needle)):
                if i+j>=len(haystack) or needle[j] != haystack[i+j]:
                    found = False
                    break
            if found:
                return i
        return -1
            
        