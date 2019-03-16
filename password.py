a,b = map(str,input("").split())
res = ""
if(len(a) < len(b)):
    for i in range(len(b)-len(a)):
        a=a+str(i+1)
if(len(a) > len(b)):
    for i in range(len(a)-len(b)):
        b=b+str(i+1)
for i in range(len(a)):
    res = res+ a[i]+b[i]
print(res)
