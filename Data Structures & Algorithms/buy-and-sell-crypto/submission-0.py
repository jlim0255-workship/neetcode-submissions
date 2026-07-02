class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers

        l, r = 0, 1

        maxProfit = 0

        # this loop breaks when r == len(prices)
        while r < len(prices):
            # if ascending trend
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)

            # if descending trend
            else:
                # replace l with r
                l = r
            
            # r must keep going
            r += 1

        return maxProfit