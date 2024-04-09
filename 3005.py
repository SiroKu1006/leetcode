import collections
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        max_a = -1
        ans = 0
        for i in collections.Counter(nums).most_common():
            if max_a == -1 or max_a == i[1]:
                max_a = i[1]
                ans += i[1]
        return ans


s = Solution()
print(s.maxFrequencyElements([1,2,2,2,3,1,4]))