s  = list(map(str,input().split()))
for i in range(len(s)):
    s[i] = s[i][::-1]
print(" ".join(map(str,s)))
