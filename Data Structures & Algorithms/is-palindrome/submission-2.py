class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer 
        l, r = 0, len(s) - 1

        # remove invalid char
        while l < r:
            # replace while loop with if also work?
            while l < r and not s[l].isalnum():
                l += 1

            while r > l and not s[r].isalnum():
                r -= 1

            # actual checking
            if s[l].lower() != s[r].lower():
                return False
            
            else:
                l += 1
                r -= 1
        return True