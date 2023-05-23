n=int(input())
l=list(map(int,input().split()))
p=1
for i in l:
    p*=i
for j in l:
    print(p//j,end=" ")  