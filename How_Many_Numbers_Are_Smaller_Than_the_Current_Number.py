n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if(i!=j and l[i]>l[j]):
            c+=1
    print(c,end=" ")