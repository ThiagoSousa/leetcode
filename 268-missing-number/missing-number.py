class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_n = max(nums)
        aux_vector = [0 for i in range(max_n+1)]
        for i in nums:
            aux_vector[i] = 1
        for i in range(len(aux_vector)):
            if aux_vector[i] == 0:
                return i
        return max_n+1
