# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left<right:
            middle = left+int((right-left)/2)
            print(left, right, middle)
            if isBadVersion(middle):
                right = middle
            else:
                left = middle+1
        return left