class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l=1
        r=x+1
        while l<r:
            if l*l==x:
                return l
            elif l*l<x:
                l+=1
            else:
                return l-1

        