n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    c=1
    if(i==(n-1)):
        print(0,end=" ")
    else:
        for j in range(i+1,n):
            if(l[i]<l[j]):
                print(c,end=" ")
                break
            else:
                c+=1
        else:
            print(0,end=" ")