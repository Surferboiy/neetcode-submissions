class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        mainstring=""
        w1=len(word1)
        w2=len(word2)
        while(i!=w1 and j!=w2):
            mainstring+=word1[i]
            i+=1
            mainstring+=word2[j]
            j+=1
        if(i<w1):
            mainstring+=word1[i:]
        elif(j<w2):
            mainstring+=word2[j:]
        return mainstring

            
