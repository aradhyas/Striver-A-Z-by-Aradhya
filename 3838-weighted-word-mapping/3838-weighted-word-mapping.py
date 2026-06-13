# ord(c) gives the ascii value so we subtract it from a which is 97, so in that way we can start from 0 and map it to weights array
# in mapped we are taking reverse of ord, we are taking chr from reverse

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''
        for word in words:
            w = 0
            for c in word:
                index = ord(c) - ord('a')
                w+=weights[index]

            new_index = w % 26
            mapped = chr(ord('z') - new_index)
            res += mapped
        
        return res