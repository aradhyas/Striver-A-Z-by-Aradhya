class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in final:
                final[key] = []
            
            final[key].append(word)
        
        return list(final.values())