class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_mag = {}
        for i in range(len(magazine)):
            if magazine[i] in freq_mag:
                freq_mag[magazine[i]]+=1
            else:
                freq_mag[magazine[i]] = 1


        for i in range(len(ransomNote)):
            if ransomNote[i] not in freq_mag or freq_mag[ransomNote[i]] == 0:
                return False
            if ransomNote[i] in freq_mag:
                freq_mag[ransomNote[i]] -= 1
        
        return True