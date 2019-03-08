import math
s = input("")
ans = 0
for i in range(len(s)):
    x = int(s[i])
    if(i != len(s)-1):
        pow = int(s[i+1])
    else:
        pow = int(s[0])
    ans+= math.pow(x,pow)
print(int(ans))
