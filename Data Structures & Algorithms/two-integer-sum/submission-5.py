class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if n==2:
            return [0,1]
        
        vals=[nums[0]]
        for i in range(1,n):
            req=target-nums[i]
            if req in vals:
                return [vals.index(req),i]

            vals.append(nums[i])
        

        