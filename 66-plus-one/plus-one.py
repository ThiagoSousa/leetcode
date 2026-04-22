class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        i = len(digits)-1
        while remainder > 0 and i>=0:
            digits[i] += remainder
            if digits[i]>=10:
                digits[i] = 0
                remainder = 1
            else:
                remainder = 0
            i-=1
        if remainder>0:
            digits[:] = [1]+digits
        return digits
        
        
        