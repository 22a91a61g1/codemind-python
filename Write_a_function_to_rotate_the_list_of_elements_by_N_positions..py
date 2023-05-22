n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
r=int(input())
for i in range(r):
    a=l[0]
    l.pop(0)
    l.append(a)
print(*l[::-1])