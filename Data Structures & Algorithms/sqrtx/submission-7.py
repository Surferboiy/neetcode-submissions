class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        for i in range(1,x+1):
            if x==i*i:
                return i
            elif x<i*i:
                return i-1
