from traceback import print_tb
from typing import Counter


words = list(map(str,input().split(',')))
k = int(input())

ans = []
ca = Counter(words)
ks = dict(sorted(ca.items(), key=lambda item: item[1],reverse=True))
temp = max(list(ks.values()))
case = []
for a in ks:
    if ks[a]==temp:
        case.append(a)
    else:
        case.sort()
        for g in case:
            ans.append(g)
        case = []
        temp = ks[a]
        case.append(a)
if case != []:
    case.sort()
    for g in case:
        ans.append(g)         
print(ans[:k])

