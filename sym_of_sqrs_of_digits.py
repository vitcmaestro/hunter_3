import math
n = input("")
ans = 0
for i in n:
    z = int(i)
    ans += math.pow(z,2)
print(int(ans))
