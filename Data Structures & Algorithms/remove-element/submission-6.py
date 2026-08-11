class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=len(nums)-1
        count=0

        while(l<len(nums) and l<=r):
            while(r>0 and nums[r]==val):
                r=r-1
            if l<=r and nums[l]==val:
                nums[l],nums[r]=nums[r],nums[l]
                r=r-1
            l=l+1
            print(nums)

        for i in nums:
            if i!=val:
                count=count+1
        return count

        