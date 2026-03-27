class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        solutions = []

        def dfs(p, open, closed):

            if len(p) == 2*n:
                solutions.append(p)
                return

            if open<n:
                dfs(p+"(", open + 1, closed)
            if closed<open:
                dfs(p+")", open, closed + 1)
            
        dfs("", 0, 0)

        return solutions
        