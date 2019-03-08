def ispal(x):
    li = list(x)
    rev = li[::-1]
    if(li == rev):
        return True
    else:
        return False
s = input()
ans = 0
for i in range(1,len(s)):
    for j in range(i):
        y = s[j:i]
        if(ispal(y) and len(y)>ans):
            ans = len(y)
print(ans)
