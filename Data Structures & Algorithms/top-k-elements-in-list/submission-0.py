class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict={}
        for i in nums:
            if i not in countdict:
                countdict[i]=1
            else:
                countdict[i]+=1
        sorted_val=sorted(countdict.items(),key=lambda item:item[1],reverse=True)
        variablelist=[]
        for i in range(k):
            variablelist.append((sorted_val[i][0]))
        return variablelist
        