class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr=set()
        max_len=0
        i=0
        j=0
        while(j<len(s)):
            if s[j] in substr:
                substr.remove(s[i])
                i+=1
            else:
                substr.add(s[j])
                j+=1
            max_len=max_len if len(substr)<max_len else len(substr)
        return max_len
        
        