n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    a=64
    for k in range(i):
        a+=1
        print(chr(a),end="")
    for l in range(i-1):
        a-=1
        print(chr(a),end="")
    print('')