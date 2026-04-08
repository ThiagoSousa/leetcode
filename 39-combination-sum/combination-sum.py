class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        solutions = []
        
        def backsearch(candidates, target, partial):

            # print(candidates, target, partial)

            if target == 0:
                solutions.append(partial)
                return

            for i in range(len(candidates)):
                if candidates[i]<=target:
                    backsearch(candidates[i:], target-candidates[i], partial+[candidates[i]])

        backsearch(candidates, target, [])

        return solutions