class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window, variable size
        l = 0
        dct = {}
        maxlen = 0

        for r in range(len(s)):
            # value of this key += 1
            dct[s[r]] = 1 + dct.get(s[r], 0)
            
            # invalid condition
            # get the most frequent value in the dict       
            while (r - l) + 1 - max(dct.values()) > k:
                dct[s[l]] -= 1
                l += 1
                
            maxlen = max(maxlen, (r - l) + 1)

        return maxlen