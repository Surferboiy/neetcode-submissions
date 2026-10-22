class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for i in strs:
            word="".join(sorted(i))
            if word not in anagram:
                anagram[word]=[i]
            else:
                anagram[word].append(i)
        main=[]
        for k,v in anagram.items():
            main.append(v)
        return main

            

        

        
                    





                    
        