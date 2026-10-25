class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1,l2=0,0
        r1,r2=m,n
        copyarr=[]
        while(l1<r1 and l2<r2):
            if nums1[l1]>nums2[l2]:
                copyarr.append(nums2[l2])
                l2+=1
            elif nums1[l1]==nums2[l2]:
                copyarr.append(nums1[l1])
                copyarr.append(nums2[l2])
                l1+=1
                l2+=1
            else:
                copyarr.append(nums1[l1])
                l1+=1

        if l1<r1:
            for i in range(l1,r1):
                copyarr.append(nums1[i])
        if l2<r2:
            for i in range(l2,r2):
                copyarr.append(nums2[i])
        nums1[:]=copyarr
        return nums1
                    
        