s = input("")
t = input("")
x = 0
res=""
res1 = ''
for i in s:
    if(i in t[x:]):
        res = res+i
        x = t.index(i)+1
x = 0
for i in t:
    if(i in s[x:]):
        res1 = res1+i
        x = s.index(i)+1
if(len(res)>= len(res1)):
    print(res)
else:
    print(res1)
