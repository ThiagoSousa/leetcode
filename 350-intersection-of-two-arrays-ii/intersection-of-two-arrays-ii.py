class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        for n in nums1:
            d1[n] = d1.get(n,0)+1
        
        d2 = {}
        for n in nums2:
            d2[n] = d2.get(n,0)+1
            
        out = []
        for n in d1:
            if n in d2:
                if d1[n]<=d2[n]:
                    out += [n] * d1[n]
                else:
                    out += [n] * d2[n]
        return out