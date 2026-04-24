class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for day in prices:
            if day < min_price:
                min_price = day
            if (profit := day - min_price) > max_profit:
                max_profit = profit
            
        return max_profit
        