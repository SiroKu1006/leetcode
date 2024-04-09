class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        ans = 0
        for a in range(len(tickets)):
            if a < k:
                ans += min(tickets[a],tickets[k])
            elif a == k:
                ans += tickets[k]
            else:
                ans += min(tickets[a],tickets[k]-1)
        return ans
s = Solution()
print(s.timeRequiredToBuy([1,10],0)) # 6
print(s.timeRequiredToBuy([5,1,1,1],0 )) # 8

# 232
# 321
# 212
# 121
# 21
# 11
# 1

# 5111
# 1141
# 141
# 14
# 4
# 3
# 2
# 1
# 0

# 5121
# 1214