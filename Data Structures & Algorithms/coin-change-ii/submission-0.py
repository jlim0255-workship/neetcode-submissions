class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, a):

            # base case(s)
            # we can sum to the amount
            if a == amount:
                return 1
            
            # if we cannot sum to the amount
            if a > amount:
                return 0
            
            # index out of bound, return 0
            if i == len(coins):
                return 0
            
            # its already exsists
            if (i, a) in cache:
                return cache[(i, a)]
            
            # go right and go down
            # dfs(i, a + coins[i]) -> go right, a is current amount + coins[i], go coins[i] steps to the right

            # dfs(i + 1, a) -> go to the next coin (1 row below) at the same amount level
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)

            return cache[(i, a)]
        
        return dfs(0,0)