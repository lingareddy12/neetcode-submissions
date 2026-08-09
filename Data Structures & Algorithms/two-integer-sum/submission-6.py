class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d={}
        for i,n in enumerate(nums):
            req=target-n
            if req in d:
                return [d[req],i]
            
            d[n]=i
        
        