class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        solutions = []
        candidates.sort()

        def backsearch(candidates, target, partial):

            if target < 0:
                return

            if target == 0:
                # if partial not in solutions:
                solutions.append(partial)
                return

            for i in range(len(candidates)):
                if i>0 and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]<=target:
                    backsearch(candidates[i+1:], target-candidates[i], partial+[candidates[i]])
                

        backsearch(candidates, target, [])

        return solutions
