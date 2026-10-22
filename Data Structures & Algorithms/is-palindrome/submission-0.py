class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        flag=0
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if(s[l].lower()!=s[r].lower()):
                flag=1
                break
            else:
                l+=1
                r-=1
        if flag==1:
            return False
        else:
            return True


        