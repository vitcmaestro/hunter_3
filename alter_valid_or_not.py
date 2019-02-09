import collections
import math
s = input("")
freq = collections.Counter(s)
maxer = 0
ltr = s[0]
mid = math.ceil(len(s)//2)
for x,y in freq.items():
    if(y>maxer):
        maxer = y
        ltr = x
if(len(s) == 1):
    print("yes")
elif(y>= mid):
    print("no")
else:
    print("yes")
