class Solution:
    def rec(self,nums, index, currentOR, maxOR, count):
        if currentOR == maxOR :
            count[0] += 1
        for i in range(index,len(nums)):
            self.rec(nums, i+1 , currentOR|nums[i], maxOR, count)
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        maxOr = 0
        for num in nums:
            maxOr |= num
        count = [0]
        self.rec(nums, 0, 0, maxOr, count)

        return count[0]


s = Solution()
print(True if s.countMaxOrSubsets([3,1]) == 2 else s.countMaxOrSubsets([3,1]))
print(True if s.countMaxOrSubsets([2,2,2]) == 7 else s.countMaxOrSubsets([2,2,2]))
print(True if s.countMaxOrSubsets([3,2,1,5]) == 6 else s.countMaxOrSubsets([3,2,1,5]))