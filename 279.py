n = int(input())

num = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961]
temp = len(num)-1
ans = 5
while num[temp]>n:
    temp-=1

while temp > 0:
    for i in range(temp,-1,-1):
        an = 0
        m = n
        g = i
        while m > 0:
            if num[g]>m:
                g-=1
            else:
                m -= num[g]
                an += 1
        ans = min(ans,an)
    # if an > 4:
    #     break
    temp -= 1
print(ans)
