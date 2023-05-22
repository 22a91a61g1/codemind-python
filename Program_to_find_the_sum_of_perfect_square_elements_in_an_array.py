n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if(i**(0.5))%1==0:
        s+=i
print(s)