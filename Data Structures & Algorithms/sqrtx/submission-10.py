class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l=1
        r=x+1
        while l<=r:
            mid=(l+r)//2
            sq=mid*mid
            if sq==x:
                return mid
            elif sq<x:
                l=mid+1
            else:
                r=mid-1
        return r

        