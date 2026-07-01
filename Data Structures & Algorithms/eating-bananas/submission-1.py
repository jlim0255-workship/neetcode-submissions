class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hours_needed(piles, k):
            return sum(math.ceil(p / k) for p in piles)

        # we are not searching the array, we are structuring 1..k(h)!
        # so start from 1
        l, r = 1, max(piles)

        # this loop will break when l == r, so we have to make sure
        # NO l == r condition inside the loop, else we will get infinite loop
        while l < r:
            mid = l + ( r - l) // 2

            if hours_needed(piles, mid) <= h:
                r = mid

            else:
                l = mid + 1

        return l