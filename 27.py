class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ans] = nums[i]
                ans += 1
        return ans

sol = Solution()
print(sol.removeElement([3,2,2,3],3),2)
print(sol.removeElement([0,1,2,2,3,0,4,2],2),5)
print(sol.removeElement([3,3],3),0)