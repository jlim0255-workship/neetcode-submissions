class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dct1 = {}
        dct2 = {}

        # loop for s
        for index, char in enumerate(s):
            key = char
            
            # update the count based on this key
            dct1[key] = 1 + dct1.get(key, 0)

        # loop for t
        for index, char in enumerate(t):
            key = char
            
            # update the count based on this key
            dct2[key] = 1 + dct2.get(key, 0)

        if (dct1 == dct2):
            return True
        
        return False