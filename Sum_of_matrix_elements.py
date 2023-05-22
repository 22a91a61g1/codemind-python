a=int(input())
b=int(input())
s=0
for i in range(a):
    l=list(map(int,input().split()))
    s+=sum(l)
print(s)