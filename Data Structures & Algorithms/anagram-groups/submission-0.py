class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        main=[]
        for word in strs:
            signature=''.join(sorted(word))
            if signature in s:
                s[signature].append(word)
            else:
                s[signature]=[word]
        
        for key,value in s.items():
            main.append(value)
        return main



