n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(n):
    s=0
    for j in range(i,n):
        s+=l[j]
        if(s==k):
            c+=1
            break
        elif(s>k):
            break
print(c)