class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==2:
            return [0,1]
        
        vals=[nums[0]]
        for i in range(1,len(nums)):
            req=target-nums[i]
            if req in vals:
                return [vals.index(req),i]

            vals.append(nums[i])
        

        