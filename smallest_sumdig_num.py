def sumdig(x):
    ans = 0
    while(x>0):
        rem = x%10
        ans = ans+rem
        x = x//10
    return ans
n = int(input())
if(len(str(n)) == 1):
    print(n)
else:
    c = True
    x = 10
    while(c):
        z = sumdig(x)
        if(z == n):
            print(x)
            c = False
        x+=1
