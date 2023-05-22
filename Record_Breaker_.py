for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(i==0):
            if(l[i+1]<l[i]):
                c+=1
        elif(i==n-1):
            a=max(l[:i])
            if(l[i]>a):
                c+=1
        else:
            a=max(l[:i])
            if(l[i]>a and l[i]>l[i+1]):
                c+=1
    print("Case #%d:"%(_+1),c)