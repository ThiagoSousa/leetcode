class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x<0 else False
        number = [i for i in str(x).replace("-", "")]
        for i in range(int(len(number)/2)):
            aux = number[i]
            number[i] = number[len(number)-i-1]
            number[len(number)-i-1] = aux
        number = int("".join(number))
        if is_negative:
            number = number*-1
        if number>2**31-1 or number<-2**31-1:
            return 0
        return number
            
        