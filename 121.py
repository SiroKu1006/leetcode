class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        now , ans = prices[0] , 0
        for i in prices:
            if i < now:
                now = i
            elif i-now > ans:
                ans = i-now
        return ans


ans = Solution()
print(ans.maxProfit([7,1,5,3,6,4]),5)
print(ans.maxProfit([1,2,3,4,5]),4)
print(ans.maxProfit([7,6,4,3,1]),0)

        # ans = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i] > ans:
        #             ans = prices[j]-prices[i]
        # return ans

