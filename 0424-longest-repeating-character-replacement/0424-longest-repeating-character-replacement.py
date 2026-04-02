class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxFreq = 0
        best = 0

        for r, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            maxFreq = max(maxFreq, count[ch])

            # if more than k chars need to be replaced, shrink window
            while (r - l + 1) - maxFreq > k:
                left_ch = s[l]
                count[left_ch] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best