# 1.py pro

# TLE
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         if max(nums)< 0 or min(nums)>0:
#             return []
#         if len(nums) == 3 and sum(nums)==0:
#             return [nums]
#         ans = []
#         for i in range(len(nums)):
#             if nums[i] > 0 :
#                 break
#             cas = 0
#             target = 0 - nums[i]
#             cc = nums[i+1:]
#             if len(cc) == 3 and sum(cc)==0:
#                 return [cc]
#             for n in cc:
#                 li_ans = []
#                 cas = target - n 
#                 if cas in cc:
#                     if cas == n:
#                         if cc.count(n) > 1:
#                             li_ans = [nums[i],n, n]
#                     else:
#                         li_ans = [nums[i],n, cas]
#                 li_ans.sort()
#                 if li_ans != [] and li_ans not in ans:
#                     ans.append(li_ans)
#         return ans


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0 :
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0 :
                    left += 1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    now_left = nums[left]
                    now_right = nums[right]
                    while left < right and nums[left] == now_left:
                        left += 1
                    while left < right and nums[right] == now_right:
                        right -= 1
        return ans
nums = [1,3,5]
s = Solution()
print(s.threeSum(nums))
