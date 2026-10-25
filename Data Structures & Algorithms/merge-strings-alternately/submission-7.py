class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1,l2=0,0
        fword=[]
        while(l1<len(word1) and l2<len(word2)):
            fword.append(word1[l1])
            fword.append(word2[l2])
            l1+=1
            l2+=1
        fword.append(word1[l1:])
        fword.append(word2[l2:])
        return "".join(fword)

        