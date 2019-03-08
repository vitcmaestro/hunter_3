st1 = input("")
st2 = input("")
k = 0
li = []
for i in range(min(len(st1),len(st2))):
    li.append(st2[i]+st1[i])
    k+=1
if(len(st1)>len(st2)):
    while(k<len(st1)):
        li.append(st1[j])
        k+=1
elif(len(st1)<len(st2)):
    while(k<len(st2)):
        li.append(st2[j])
        k+=1
print("\n".join(map(str,li)))
