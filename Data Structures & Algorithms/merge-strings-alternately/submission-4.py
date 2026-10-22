class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        mainstring=[]
        while(i<len(word1) and j<len(word2)):
            mainstring.append(word1[i])
            mainstring.append(word2[j])
            i+=1
            j+=1
        mainstring.append(word1[i:])
        mainstring.append(word2[j:])
        return "".join(mainstring)
        