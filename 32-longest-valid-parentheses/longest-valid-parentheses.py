class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        queue = []
        intervals = []

        for i in range(len(s)):
            if s[i] == "(":
                queue.append(i)
            if s[i] == ")":
                if len(queue)>0:
                    j = queue.pop()
                    intervals.append([j,i])
        
        aux_vector = [0 for i in range(len(s))]
        for x,y in intervals:
            for i in range(x,y+1):
                aux_vector[i] = 1

        max_length = 0
        i = 0
        while i<len(s):
            count = 0
            while i<len(s) and aux_vector[i] == 1:
                count += 1
                i +=1
            max_length = max(count, max_length)
            i += 1

        return max_length

