class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majset={}
        for i in nums:
            if i in majset:
                majset[i]+=1
            else:
                majset[i]=1
        for key,val in majset.items():
            if val>len(nums)/2:
                return key