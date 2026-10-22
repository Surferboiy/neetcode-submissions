class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        leng=len(nums)
        for i in range(leng):
            for j in range(i):
                if nums[i]==nums[j]:
                    if abs(i-j)<=k:
                        return True
        return False