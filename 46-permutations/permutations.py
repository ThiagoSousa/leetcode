import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []

        def dfs(partial, missing):

            print(partial, missing)

            if len(missing) == 0:
                permutations.append(partial)
                return

            for i in range(len(missing)):
                new_missing = copy.deepcopy(missing)
                number = new_missing.pop(i)
                dfs(partial+[number], new_missing)
            
        dfs([], nums)
        return permutations
