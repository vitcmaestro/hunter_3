s = input("")
c = 0
ans = ""
for i in range(len(s)):
    if(s[i] == " "):
        ans = ans+s[i]
    elif(c%2 == 0):
        ans = ans+ s[i].upper()
        c+=1
    else:
        ans = ans + s[i]
        c+=1
print(ans)
        
