class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        # weird, correct in python tutor but wrong here   
        # s1="abc"
        # s2="lecaabee"
        # # s1 is always smaller than s2
        
        # count1 = {}
        # count2 = {}
        # for i in range(len(s1)):
        #     count1[s1[i]] = 1 + count1.get(s1[i], 0)
        
        # # pre fill the count1 and count2 dicts
        # l = 0
        # for r in range(len(s2)):
        #     count2[s2[r]] = 1 + count2.get(s2[r], 0)

        #     # if s2[r] in count1:
        #     #     count1[s2[r]] = 1 + count1.get(s2[r], 0)

        # matches = []

        # for key1 in count1:
        #     if count1[key1] != count2[key1]:
        #         return False

        # return True

        ## sliding window
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26




        