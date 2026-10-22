class Solution:
    def validPalindrome(self, s: str) -> bool:
        def val_pal(start,end):
            while(start<end):
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True

        l,r=0,len(s)-1
        while(l<r):
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return val_pal(l+1,r) or val_pal(l,r-1)
        return True 