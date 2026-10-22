class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j,s=0,0,0
        mainstring=""
        w1=len(word1)
        w2=len(word2)
        while(i!=w1 and j!=w2):
            mainstring+=word1[i]
            s+=1
            i+=1
            mainstring+=word2[j]
            s+=1
            j+=1
        if(i<w1):
            mainstring+=word1[i:]
        else:
            mainstring+=word2[j:]
        return mainstring

            
