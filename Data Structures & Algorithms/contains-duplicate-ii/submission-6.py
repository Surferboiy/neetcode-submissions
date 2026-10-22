class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup={}
        for index,num in enumerate(nums):
            if num in dup and index-dup[num]<=k:
                return True
            dup[num]=index
        return False
        