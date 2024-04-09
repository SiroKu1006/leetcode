class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0
        left = height[0]
        now = height[1]
        right = height[2]
        low = now
        high = min(left,right)
        water = 0
        all_water = 0
        while left < len(height):
            
s = Solution()
h = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(h))