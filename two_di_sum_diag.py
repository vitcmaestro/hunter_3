x = int(input(""))
a = []
ans = 0
for i in range(x):
    temp = list(map(int,input().split()))
    a.append(temp)
j = x-1
for i in range(x):
    ans+= a[i][j]
    j -=1
print(ans)
