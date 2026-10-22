class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_t={}
        dict_s={}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in dict_s:
                    dict_s[s[i]]=1
                else:
                    dict_s[s[i]]+=1
            for i in range(len(s)):
                if t[i] not in dict_t:
                    dict_t[t[i]]=1
                else:
                    dict_t[t[i]]+=1

            if dict_t==dict_s:
                return True
        return False

        