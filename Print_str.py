st1 = input("")
st2 = input("")
j = 0
for i in range(min(len(st1),len(st2))):
    print(st2[i]+st1[i])
    j+=1
if(len(st1)>len(st2)):
    while(j<len(st1)):
        print(st1[j])
        j+=1
elif(len(st1)<len(st2)):
    while(j<len(st2)):
        print(st2[j])
        j+=1
