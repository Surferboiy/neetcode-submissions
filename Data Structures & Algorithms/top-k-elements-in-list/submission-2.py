class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashdict={}
        for num in nums:
            hashdict[num]=1+hashdict.get(num,0)
        hashdict=dict(sorted(hashdict.items(),key=lambda item:item[1],reverse=True))
        return list(hashdict.keys())[:k]
        