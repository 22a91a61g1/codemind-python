
n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i-1):
        print(i-k-1,end="")
    print(0,end="")
    for l in range(i-1):
        print(l+1,end="")
    print('')
