class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*(2*len(nums))
        n=len(nums)
        for i in range(2*n):
            if i>(n-1):
                ans[i]=nums[i-n]
            else:
                ans[i]=nums[i]
        return ans

