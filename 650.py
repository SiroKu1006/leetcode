class Solution:
    def maximumSwap(self, num: int):
        num = list(map(int,list(str(num))))
        num.reverse()
        t = len(num)
        a = True
        while a:
            i = num[:t].index(max(num[:t]))
            # print(num[:t])
            for k in range(len(num[:t])-1,i-1,-1):
                if num[i] > num[k]:
                    num[i] , num[k] = num[k] , num[i]
                    a = False
                    break
            else:
                t = i
            if t<1:
                break

        num.reverse()
        return int(''.join(map(str, num)))





s = Solution()
print(int(s.maximumSwap(1993)))
print(int(s.maximumSwap(2736)))
print(int(s.maximumSwap(98368)))
print(int(s.maximumSwap(12335431)))
print(int(s.maximumSwap(99901)))