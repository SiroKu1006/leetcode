class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sc = 0
        ans = 0
        for a in s:
            if a == "R":
                sc+=1
            else:
                sc-=1
            if sc == 0:
                ans+=1
        return ans



s = Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))