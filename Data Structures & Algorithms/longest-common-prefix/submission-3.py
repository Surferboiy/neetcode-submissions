class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        final=""
        if len(strs)==1:
            return strs[0]
        for i in range(len(strs[0])):
            count=1
            for j in range(len(strs)-1):
                if strs[j][i]==strs[j+1][i]:
                    count+=1
            if count==len(strs):
                final+=strs[j][i]
            else:
                return final
        return final


        

            
        

        
        
            