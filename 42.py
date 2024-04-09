class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        n = 0
        high = 0
        low = 0
        left = 0
        right = 1
        while right < len(height)-1:
            
        return ans





sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) , 6)
print(sol.trap([4,2,0,3,2,5]) , 9)
print(sol.trap([4,2,3]) , 1)
print(sol.trap([2,0,2]) , 2)