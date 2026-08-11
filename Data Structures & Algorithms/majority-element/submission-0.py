class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count=0
        for i in nums:
            if count==0:
                m=i
                count=count+1
            elif i==m:
                count=count+1
            else:
                count=count-1
        
        return m
        