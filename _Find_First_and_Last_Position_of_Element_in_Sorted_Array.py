n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
d=0
for i in range(n):
    if(l[i]==k):
        print(i,end=" ")
        d=1
        break
else:
    print(-1,-1)
for j in range(i+1,n):
    if(l[j]==k):
        print(j,end=" ")
        break
else:
    if(d==1):
        print(i)