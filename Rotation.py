for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l=l[::-1]
    for i in range(k):
        a=l[0]
        l.pop(0)
        l.append(a)
    print(*l[::-1])