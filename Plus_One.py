n=int(input())
l=list(map(str,input().split()))
s=""
for i in l:
    s+=i
a=int(s)+1
b=str(a)
for i in b:
    print(i,end=" ")