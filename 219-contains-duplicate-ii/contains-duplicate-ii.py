class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # d = dict()
        # for i in range(len(nums)):
        #     if nums[i] in d: 
        #         for j in d[nums[i]]:
        #             if i!=j and abs(i-j)<=k:
        #                 return True
        #     else:
        #         d[nums[i]] = []
        #     d[nums[i]].append(i)
        # return False

        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = []
            d[nums[i]].append(i)            
        
        for number in d:
            print(number)
            for i in range(len(d[number])):
                for j in range(i+1, len(d[number])):
                    if abs(d[number][i]-d[number][j])<=k:
                        return True
        return False

