class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # init dp array, 
        # index until amount
        # every value is a big value
        dp = [amount + 1] * (amount+1)

        # the first item, INDEX IS AMOUNT = 0 (CURRENT SUBPROBLEM TARGET), 
        # needed 0 coin to achieve amount 0
        dp[0] = 0

        # go through dp array from 1
        # i is the current subproblem target amount
        # ex: i = 1, target amount = 1, how many coins do we need?
        for i in range(1, amount+1):
            # test with each coin we have
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])

        # if the last value is the amount we initialized (amount + 1), return -1, meaning no possible ways
        # else return the last value
        return dp[amount] if dp[amount] != amount+1  else -1
