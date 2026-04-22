class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for i in nums:
            map[i] = map.get(i,0)+1

        sorted_nums = sorted(map.items(), key=lambda x:x[1], reverse=True)

        return [sorted_nums[i][0] for i in range(k)]
        