import enum
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        for idx, price in enumerate(prices):
            if (price < minPrice):
                minPrice = price
            elif (price - minPrice > maxProfit):
                maxProfit = price - minPrice
        return maxProfit
                
    
if __name__ == "__main__":
    instance = Solution
    prices: List[int] = [2,1,2,0,1]
    print(instance.maxProfit(instance, prices))