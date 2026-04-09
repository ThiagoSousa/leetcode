class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [i for i in s if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57)]
        
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True