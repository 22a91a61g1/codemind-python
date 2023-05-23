n=int(input())
l=list(map(int,input().split()))
ma=0
for i in range(n-1):
    if(l[i]==1):
        c=1
        for j in range(i+1,n):
            if(1==l[j]):
                c+=1
            else:
                break
        if(ma<c):
            ma=c
print(ma)