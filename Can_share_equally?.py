a,b=map(int,input().split())
if(a%2==1):
    print("NO")
elif(a==0 and b%2==1):
    print("NO")
else:
    print("YES")