class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma ,su = nums[0] , 0
        for i in nums:
            su+=i
            ma = max(ma,su)
            if su <= 0 :su = 0
        return ma
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)
print(sol.maxSubArray([1]),1)
