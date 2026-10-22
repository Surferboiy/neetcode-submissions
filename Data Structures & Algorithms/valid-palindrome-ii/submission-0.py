class Solution():
    def validPalindrome(self,s:List[str])->bool:
        def check_pal(l,r):
            while(l<r):
                if(s[l]!=s[r]):
                    return False
                l+=1
                r-=1
            return True
        l,r=0,len(s)-1
        while l<r:
            if(s[l]!=s[r]):
                return check_pal(l+1,r) or check_pal(l,r-1)
            l+=1
            r-=1
        return True
        
