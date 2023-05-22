n=int(input())
if(n<3):
    print("The pattern is not possible")
else:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print("")
    for k in range(n-1,0,-1):
        for l in range(k):
            print("*",end="")
        print("")
        