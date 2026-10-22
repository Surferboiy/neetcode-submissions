class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest=strs[0]
        sstring=""
        
        for i in strs:
            if len(i)<len(smallest):
                smallest=i
        for i in range(len(smallest)):
            count=0
            for j in strs:
                if(smallest[i]!=j[i] and i==0):
                    return ""
                elif smallest[i]==j[i]:
                    count=count+1
            if count==len(strs):
                sstring=sstring+smallest[i]
        return sstring


        


            
        
        
        