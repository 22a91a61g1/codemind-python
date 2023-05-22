n=int(input())
l=list(map(int,input().split()))
c1=0
c2=0
for i in l:
    if(i==0):
        c1+=1
    else:
        c2+=1
for _ in range(c1):
    print(0,end=" ")
for _ in range(c2):
    print(1,end=" ")