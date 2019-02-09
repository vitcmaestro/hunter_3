s = input("")
lis = list(s)
d = 0
for i in range(-1,-(len(s)),-1):
    if(ord(lis[i])>ord(lis[i-1])):
        lis[i],lis[i-1] = lis[i-1],lis[i]
        d = 1
        break
else:
    d = 0
if(d == 0):
    print("-1")
else:
    print("".join(map(str,lis)))
