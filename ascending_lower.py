x = int(input(""))
alpha = list(map(str,input().split()))
for i in range(x):
    alpha[i] = alpha[i].lower()
alpha.sort()
print("\n".join(map(str,alpha)))
