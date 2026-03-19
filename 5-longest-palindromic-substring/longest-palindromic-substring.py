class Solution:
    def is_palindrome(self, s: str) -> bool:
        for i in range(int(len(s)/2)):
            if s[i] != s[i*-1-1]:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        palindrome_size = 1
        largest_palindrome = s[0]

        for i in range(len(s)):
            print(i, s[i])

            # check odd
            start = i-1
            end = i+1
            while start>=0 and end<len(s) and s[start]==s[end]:
                if end-start>=palindrome_size:
                    palindrome_size = end - start
                    largest_palindrome = s[start:end+1]
                start -=1
                end+=1

            # check even
            start = i
            end = i+1
            while start>=0 and end<len(s) and s[start]==s[end]:
                if end-start>=palindrome_size:
                    palindrome_size = end - start
                    largest_palindrome = s[start:end+1]
                start -=1
                end+=1
            
        return largest_palindrome
                

        
            

