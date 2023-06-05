n=int(input())
a=[]
l1=[]
for i in range(n):
    l=list(map(str,input().split()))
    a.append(l[1])
    l1.append(l[0])
    l1.append(l[1])
for i in a:
    if(l1.count(i)==1):
        print(i)
        break