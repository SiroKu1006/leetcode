class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s)-1
        now = s[left]
        while left <= right:
            # print(left,right,now)
            if s[right] == s[left] and left != right:
                now = s[left]
            elif  left == right:
                break
            else:
                if now not in [s[right],s[left]]:
                    break
            if s[left] == now:
                left += 1
            if s[right] == now:
                right -= 1


        return right - left + 1



            
            
            

s = Solution()
print(s.minimumLength("abc"))