class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        j = 0
        while j<len(prices):
            profit = prices[j] - minPrice
            if prices[j] < minPrice:
                minPrice = prices[j]
                profit = prices[j] - minPrice
            maxProfit = max(profit,maxProfit)
            j += 1
        return maxProfit        


            

        
