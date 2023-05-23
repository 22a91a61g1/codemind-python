n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(n):
    for j in range(i+1,n):
        d.append(l[i]-l[j])
m=(min(d))
if(m<1):
    print((-1)*m)
else:
    print(0)