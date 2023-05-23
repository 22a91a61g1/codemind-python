n=int(input())
l=list(map(int,input().split()))
s=set(l)
c=[]
for i in s:
    if(l.count(i)==1):
        c.append(i)
if(len(c)==0):
    print(-1)
else:
    print(max(c))