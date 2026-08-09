class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==2:
            return [0,1]
        
        d={}
        d[0]=nums[0]
        for i in range(1,len(nums)):
            req=target-nums[i]
            for k,v in d.items():
                if v==req:
                    return [k,i]

            d[i]=nums[i]
        

        