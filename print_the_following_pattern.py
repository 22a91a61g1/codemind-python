n=int(input())
a=64+n
for i in range(n):
    for j in range(n-i):
        print(chr(a),end=" ")
    a-=1
    print("")