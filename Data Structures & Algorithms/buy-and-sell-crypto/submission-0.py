class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_selling=0
        min_buying=0
        largest=0
        for i in range(n):
            for j in range(i+1,n):
                min_buying=prices[i]
                max_selling=prices[j]
                largest=max(largest,max_selling-min_buying)
        if largest<=0:
            return 0
        return largest
            





                
            
            



        