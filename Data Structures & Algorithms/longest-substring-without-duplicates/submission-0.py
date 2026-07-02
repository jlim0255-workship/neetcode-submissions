class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window -> variable size

        # at start, l == r
        l = 0

        # set for duplication and lookup
        sett = set()

        maxlen = 0

        # go through the str
        # for r, char in enumerate(s): -> this is wrong
        for r in range(len(s)):
            
            # if window is invalid
            # remove the duplicate char of s[l]
            # advance l
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            # if window is valid
            # add s[r] into set
            sett.add(s[r])

            currlen = (r - l) + 1
            maxlen = max(currlen, maxlen)

        return maxlen