class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        freq_pat = {}
        freq_words = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in freq_pat and freq_pat[char]!=word:
                return False

            if word in freq_words and freq_words[word]!=char:
                return False
            
            freq_pat[char] = word
            freq_words[word] = char
        
        return True
