class Solution:
    def isValid(self, s: str) -> bool:
        prst=[]
        for i in range(len(s)):
            if (s[i] in ('(','{','[')):
                prst.append(s[i])
            elif(len(prst)==0):
                return False
            elif(s[i]==")" and prst[-1]=="("):
                prst.pop()
            elif(s[i]=="}" and prst[-1]=="{"):
                prst.pop()
            elif(s[i]=="]" and prst[-1]=="["):
                prst.pop()
            else:
                return False
        if(len(prst)==0):
            return True
        return False
        