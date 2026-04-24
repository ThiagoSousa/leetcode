class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        def dfs(partial):

            if len(partial) == k:
                combinations.append(partial)
                return
            start = 1
            if len(partial)>0:
                start = partial[-1]+1
            for i in range(start, n+1):
                dfs(partial+[i])

        dfs([])

        return combinations
