s = input("")
lis = list(s)
d = 0
for i in range(-1,-(len(s)),-1):
    for j in range(i-1,-(len(s)),-1):
        if(ord(lis[i])>ord(lis[j])):
            lis[i],lis[j] = lis[j],lis[i]
            d = 1
            print("".join(map(str,lis)))
            exit(0)
if(d == 0):
    print("-1")
