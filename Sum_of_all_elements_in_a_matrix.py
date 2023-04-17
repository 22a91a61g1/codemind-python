n,m=map(int,input().split())
s=0
for i in range(n):
    lst=list(map(int,input().split()))
    s+=sum(lst)
print(s)

