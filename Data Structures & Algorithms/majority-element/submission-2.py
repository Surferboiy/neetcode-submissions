class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for key,val in count.items():
            if val>len(nums)//2:
                break
        return key

        