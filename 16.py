# 15.py pro
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > target:
                    if abs(ans - target) > abs(s - target):
                        ans = s
                    right -= 1
                elif s < target :
                    if abs(ans - target) > abs(s - target):
                        ans = s
                    left += 1
                else:
                    return target
        return ans
nums = [1,1,1,0]

s = Solution()
print(s.threeSumClosest(nums,100))
