class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            nums.append(target)
            nums.sort()
            return nums.index(target)