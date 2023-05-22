for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in range(a-1):
        s=l[i]
        for j in range(i+1,a):
            s+=l[j]
            if(s==b):
                print(i+1,j+1)
                c=1
                break
            elif(s>b):
                break
        if(c==1):
            break
    else:
        print(-1)