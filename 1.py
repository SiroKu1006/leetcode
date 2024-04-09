class Solution:
    def twoSum(self, nums: list[int], target: int) -> list [int]:
        cas = 0
        for n in nums:
            cas = target - n
            if cas in nums:
                if cas == n:
                    if nums.count(n) > 1:
                        return [nums.index(n), nums.index(n, nums.index(n)+1)]
                else:
                    return [nums.index(n), nums.index(cas)]
        return [0]
    


lis = [2, 7, 11, 15]
target = 9
Solution()
print(Solution.twoSum(lis, target))