n,k,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    a=l[-1]
    l.pop()
    l.insert(0,a)
for j in range(q):
    print(l[int(input())])