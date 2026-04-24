class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []

        def dfs(partial):
            subsets.append(partial)

            if len(partial) == len(nums):
                return

            for i in range(len(nums)):
                if len(partial)==0 or nums[i] > partial[-1]:
                    dfs(partial+[nums[i]])
        
        dfs([])
        return subsets
