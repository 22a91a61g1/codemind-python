n=int(input())
l=list(map(int,input().split()))
for i in range(1,max(l)+1):
    if(i not in l):
        print(i)
        break
else:
    print(i+1)