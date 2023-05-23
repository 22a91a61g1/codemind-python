n=int(input())
l=list(map(int,input().split()))
m=n//2
d={}
for i in l:
    if(i not in d):
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if(v>m):
        print(k)