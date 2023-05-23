n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
l2=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n1):
    if(k<=l2[i] and k>=l1[i]):
        c+=1
print(c)