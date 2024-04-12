class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        left = 0
        right = len(height)-1
        old_high = 0
        while left < right:
            if old_high < min(height[left],height[right]):
                new_high = min(height[left],height[right])
                ans += (new_high-old_high)*(right-left)
                old_high = new_high
            if height[left] <= height[right]:
                left += 1
                ans -= min(height[left],old_high)
            else:
                right -= 1
                ans -= min(height[right],old_high)
        return ans





sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) , 6)
print(sol.trap([4,2,0,3,2,5]) , 9)
print(sol.trap([4,2,3]) , 1)
print(sol.trap([2,0,2]) , 2)