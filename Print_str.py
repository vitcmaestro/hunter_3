st1 = input("")
st2 = input("")
j = 0
li = []
for i in range(min(len(st1),len(st2))):
    li.append(st2[i]+st1[i])
    j+=1
if(len(st1)>len(st2)):
    while(j<len(st1)):
        li.append(st1[j])
        j+=1
elif(len(st1)<len(st2)):
    while(j<len(st2)):
        li.append(st2[j])
        j+=1
print("\n".join(map(str,li)))
