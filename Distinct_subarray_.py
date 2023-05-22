l=int(input())
r=int(input())
c=0
for i in range(l,r+1):
    s=i
    if(s%2==1):
        c+=1
    for j in range(i+1,r+1):
        s+=j
        if(s%2==1):
            c+=1
print(c)