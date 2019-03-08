x = int(input(""))
a = []
ans = 0
for i in range(x):
    temp = list(map(int,input().split()))
    a.append(temp)
for i in range(x):
    ans+= a[i][i]
print(ans)
