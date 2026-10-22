class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_buying=prices[0]
        max_profit=0
        for i in range(n):
            profit=prices[i]-min_buying
            max_profit=max(max_profit,profit)
            min_buying=min(min_buying,prices[i])
        return max_profit


        