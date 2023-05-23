n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    m=max(l[i+1::])
    l[i]=m
l[-1]=-1
print(*l)