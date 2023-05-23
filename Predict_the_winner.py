n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in range(n):
    if(i%2==0):
        e+=l[i]
    else:
        o+=l[i]
d=abs(e-o)
if(d%4==0):
    print("X")
else:
    print("Y")