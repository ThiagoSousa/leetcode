class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = []
        for i in range(len(s)):
            if s[i] in substring:
                longest = max(longest, len(substring))
                substring = substring[substring.index(s[i])+1: ]
            substring.append(s[i])
        longest = max(longest, len(substring))
        return longest
