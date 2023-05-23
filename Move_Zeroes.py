n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in l:
    if(i==0):
        c+=1
    else:
        print(i,end=" ")
for j in range(c):
    print(0,end=" ")