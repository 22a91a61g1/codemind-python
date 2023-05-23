n=int(input())
l=list(map(int,input().split()))
for i in range(0,n,2):
    for j in range(l[i]):
        print(l[i+1],end=" ")