class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        best = 0

        while left<right:

            water = (right-left)*min(height[left], height[right])
            best = max(best, water)

            if height[left]<height[right]:
                left += 1
            elif height[left]>height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return best
