class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=len(nums)-1
        for i in range(len(nums)):
            if nums[mid]==0:
                temp=nums[low]
                nums[low]=0
                nums[mid]=temp
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                temp=nums[high]
                nums[high]=2
                nums[mid]=temp
                high-=1
                