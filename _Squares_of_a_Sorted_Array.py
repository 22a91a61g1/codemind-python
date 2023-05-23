n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    a.append(i*i)
print(*sorted(a))