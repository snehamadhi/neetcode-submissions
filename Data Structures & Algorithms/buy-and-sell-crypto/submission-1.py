class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                cur_profit=prices[i]-min_price
                max_profit=max(max_profit,cur_profit)
        return max_profit