n=int(input())
l=list(map(int,input().split()))
s=set(l)
a=[]
for i in s:
    if(l.count(i)==1):
        a.append(i)
a=sorted(a)
if(len(a)==0):
    print(-1)
else:
    print(*a)