class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_length = min([len(s) for s in strs])
        
        if max_length == 0:
            return ""
        
        prefix = []
        for i in range(max_length):
            for s in strs[1:]:
                if s[i] != strs[0][i]:
                    return "".join(prefix)
            prefix.append(strs[0][i])
            
        return "".join(prefix)
                    
        