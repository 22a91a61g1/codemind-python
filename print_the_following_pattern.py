n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            print("x",end="")
        elif(j==(n-i+1)):
            print("x",end="")
        else:
            print("0",end="")
    print("")