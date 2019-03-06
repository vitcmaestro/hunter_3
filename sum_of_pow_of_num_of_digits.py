import math
n = input("")
l = len(n)
ans = 0
for i in n:
    x = int(i)
    ans += math.pow(x,l)
print(int(ans))
