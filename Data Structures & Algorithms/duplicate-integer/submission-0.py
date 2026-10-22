class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        duplicate=False
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]==nums[j]):
                    duplicate=True
        return duplicate