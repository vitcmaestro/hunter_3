import collections
s = input("")
freq = collections.Counter(s)
maxer = 0
ltr = s[0]
for x,y in freq.items():
    if(y>maxer):
        maxer = y
        ltr = x
if(y>= (len(s)//2)):
    print("no")
else:
    print("yes")
