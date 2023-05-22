n=int(input())
l=list(map(int,input().split()))
a=l[0:n//2]
b=l[n//2:]
print(*b[::-1],end=" ")
print(*a)