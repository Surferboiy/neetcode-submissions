class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*(2*len(nums))
        for i in range(2*len(nums)):
            if i>(len(nums)-1):
                ans[i]=nums[i-len(nums)]
            else:
                ans[i]=nums[i]
        return ans

