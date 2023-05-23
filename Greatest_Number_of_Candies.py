n=int(input())
l=list(map(int,input().split()))
c=int(input())
a=max(l)
d=[]
for i in l:
    if(i+c >= a):
        print(True,end=" ")
    else:
        print(False,end=" ")