class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # @cache
        # def dp(i, n):
        #     # i is the coin selection
        #     # n is the current amount for this subproblem

        #     # we run out of coin or amount is 0
        #     if i >= len(coins) or n <= 0:
        #         return 1 if n == 0 else 0

        #     return dp(i, n - coins[i]) + dp(i+1, n)
            
        # return dp(0, amount)

        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):
            for i in range(len(coins)-1, -1, -1):
                if a - coins[i] >= 0:

                # choose to use, move to the right of coins
                # choose not to use, move down a row
                    dp[a][i] = dp[a][i+1] + dp[a - coins[i]][i]

                else:
                    dp[a][i] = dp[a][i+1]

        return dp[amount][0]        