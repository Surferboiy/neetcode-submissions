class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol={}
        count=[[] for i in range(len(nums)+1)]
        for num in nums:
            sol[num]=1+sol.get(num,0)
        for key,val in sol.items():
            count[val].append(key)
        result=[]
        for i in range(len(count)-1,0,-1):
            for n in count[i]:
                result.append(n)
                if len(result)==k:
                    return result
            
        