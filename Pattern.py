n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(k+1,end="")
    for l in range(k):
        print(k,end="")
        k=k-1
    print('')