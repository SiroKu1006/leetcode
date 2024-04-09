class Solution:
    def countAndSay(self, n: int ) :
        ans = "1"
        for i in range(n-1):
            c = ""
            j = 0
            while j < len(ans):
                now = j
                count = 0
                while True:
                    if now > len(ans)-1:
                        break
                    elif ans[now] != ans[j]:
                        break
                    else :
                        count+=1
                        now += 1
                c+= f"{count}{ans[j]}"
                j = now
            print(ans)
            ans = c
        return ans


s = Solution()
print(s.countAndSay(30))