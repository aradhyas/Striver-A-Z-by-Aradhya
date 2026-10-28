class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in freq_s and freq_s[a]!=b:
                return False
            
            if b in freq_t and freq_t[b]!=a:
                return False
            
            freq_s[a] = b
            freq_t[b] = a
        
        return True