# # 5 101
# # 6 110
# # 7 111
import math
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left > 0:
            if left == right:
                k = left
            elif int(math.log(left,2)) < int(math.log(right,2)):
                k=0
            elif int(math.log(left,2)) == int(math.log(right,2)):
                s_left = str(bin(left)).replace("0b","")
                s_right= str(bin(right)).replace("0b","")
                num = len(s_right)
                ans = "0b0"
                # print(s_left,s_right)
                for i in range(num):
                    if s_left[i] != s_right[i]:
                        ans += "0"*(num-i)
                        break
                    else:
                        ans += s_left[i]
                # print(ans)
                return int(ans,2)
        else:
            k = 0
        return k




s = Solution()
k = s.rangeBitwiseAnd(4,5)
print(k)
print(bin(17))