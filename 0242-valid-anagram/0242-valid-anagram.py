class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        
        ch1 = {}
        ch2 = {}
        for i in range(0,l1):
            if s[i] in ch1:
                ch1[s[i]]+=1
            else:
                ch1[s[i]] = 1
        
        for j in range(0,l2):
            if t[j] in ch2:
                ch2[t[j]]+=1
            else:
                ch2[t[j]] = 1

        if ch1 == ch2:
            return True
        else:
            return False