class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        queue = []

        for i in range(len(s)):
            if s[i] == "(":
                queue.append(["(",i+1])
            if s[i] == ")":
                if len(queue)>0 and queue[-1][0] == "(":
                    j = queue.pop()
                else:
                    queue.append([")", i+1])

        if len(queue) == 0:
            return len(s)

        max_length = queue[0][1]-1
        max_length = max(max_length, len(s)-queue[-1][1])

        for i in range(1,len(queue)):
            max_length = max(max_length, queue[i][1]-queue[i-1][1]-1)
        return max_length

