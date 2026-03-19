class Solution:
    def is_palindrome(self, s: str) -> bool:
        for i in range(int(len(s)/2)):
            if s[i] != s[i*-1-1]:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        palindrome_size = len(s)
        while palindrome_size>1:
            for i in range(0,len(s)-palindrome_size+1):
                candidate = s[i:i+palindrome_size]
                if self.is_palindrome(candidate):
                    return s[i:i+palindrome_size]
            palindrome_size -= 1
        return s[0]
            

        
            

