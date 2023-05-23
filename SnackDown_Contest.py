for _ in range(int(input())):
    n=int(input())
    a=[]
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
  
    for i in p:
        if(i not in a):
            a.append(i)
    for j in q:
        if(j not in a):
            a.append(j)
    if(len(a)==n):
        print("YES")
    else:
        print("NO")