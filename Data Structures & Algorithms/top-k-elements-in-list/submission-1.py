class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashdict={}
        for i in nums:
            if i not in hashdict:
                hashdict[i]=1
            else:
                hashdict[i]+=1
        sorted_hash=dict(sorted(hashdict.items(),key=lambda item:item[1],reverse=True))
        return list(sorted_hash.keys())[:k]
        