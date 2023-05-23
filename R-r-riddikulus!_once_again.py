n,a=map(int,input().split())
l=list(map(int,input().split()))
for i in range(a):
    c=l[0]
    l.pop(0)
    l.append(c)
print(*l)