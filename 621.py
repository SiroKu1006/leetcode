class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        ch = "ABCDEFGHLIJKLMNOPQRSTUVWXYZ"
        ch_cool = [0]
        now_ch = 0
        work = 0
        if n == 1:
            return len(tasks)
        while len(tasks)>0:
            if ch[now_ch] in tasks  :
                if ch_cool[now_ch] == 0:
                    ch_cool[now_ch] += 1
                    tasks.pop(tasks.index(ch[now_ch]))
                    work+=1
                else:
                    now_ch += 1
                    if now_ch+1 > len(ch_cool) and ch[now_ch] in tasks:
                        ch_cool.append(0)
            else:
                if 
                now_ch = 0






s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"],3))
